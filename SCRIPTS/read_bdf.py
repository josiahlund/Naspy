import h5py
import tempfile
import numpy as np
import warnings
from BULKDATA.BulkDataEntry import BulkDataEntry
from more_itertools import peekable


def read_bdf(path) -> object:
    with open(path) as f:
        # TODO figure out if there's a cleaner way to make f peekable.
        f = peekable(f)
        in_bulk = False
        for line in f:
            if not in_bulk:
                # Until case control cards are supported, skip all lines until BEGIN BULK statement has been read.
                if line.strip().upper() == "BEGIN BULK":
                    in_bulk = True
                    bulk_data_entries = read_bulk_data(f)
                    h5 = write_hdf5(bulk_data_entries)
        if not in_bulk:
            # BEGIN BULK is a required card for any valid Nastran job
            raise EOFError('No "BEGIN BULK" statement found.')
    return h5


def read_bulk_data(f) -> dict:
    valid_cards = [scl.__name__.upper() for scl in BulkDataEntry.__subclasses__()]
    for line in f:
        # skip blank lines and comments
        if not line.strip() or line.strip().startswith("$"):
            pass
        else:
            if line.startswith("ENDDATA"):
                break
            card_image = line[:8].strip().upper()
            # Warn when unsupported card encountered if not a continuation line
            if card_image not in valid_cards:
                if not card_image.startswith("*") and not card_image.startswith("+"):
                    warnings.warn(f'Unsupported card image found: {card_image}')
            else:
                field_data = read_card(line, f)
                # TODO see if theres a way to call a subclass directly (without having to import every subclass)
                # There's no need for this to be a list comprehension, I just want to run the subclass of
                # BulkDataEntry with name card_image
                card = [scl(*field_data) for scl in BulkDataEntry.__subclasses__()
                        if scl.__name__.upper() == card_image][0]
    cards_read = {(key := scl.__name__.upper()): (value := scl.instances) for scl in BulkDataEntry.__subclasses__()}
    return cards_read


def read_card(line: str, f) -> tuple:
    card_data = []
    while True:
        # Determine card format
        if "*" in line[:8]:
            # Card is long format
            fields_to_read = 4
            field_width = 16
        else:
            # Card is short format
            fields_to_read = 8
            field_width = 8

        card_data += [line[8 + i*field_width:8 + (i+1)*field_width].strip() for i in range(fields_to_read)]

        try:
            line = f.peek()
        except StopIteration:
            # EOF
            break
        else:
            # Check if line is empty or a comment, break
            if not line.strip() or line.strip().startswith("$"):
                break
            # Check if line could be continuation of current card
            elif not any(line[:8].startswith(c) for c in ["+", "*", " "]):
                break
            else:
                line = next(f)
    return tuple(card_data)


def write_hdf5(bulk_data_entries: dict, path=tempfile.TemporaryFile()):
    hdf5 = h5py.File(path, mode="w")
    # SCHEMA is the Nastran version.
    schema_value = 1
    hdf5.attrs.create("SCHEMA", [schema_value], dtype="int64")
    for key, value in bulk_data_entries.items():
        where = value[0].h5_path
        dtype = value[0].dtype + [("DOMAIN_ID", int)]
        count = value[0].entry_count
        sort_by = list(value[0].__dict__.keys())[0]
        data = [(tuple(card.__dict__.values())[:count] + (1,)) for card in bulk_data_entries[key]]
        cards = np.sort(np.array(data, dtype=dtype), order=sort_by)
        table = hdf5.create_dataset(where, data=cards, dtype=dtype)
        table.attrs.create("version", [0], dtype="int64")
    return hdf5
