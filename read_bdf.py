import warnings
from BULKDATA.BulkDataEntry import BulkDataEntry
from more_itertools import peekable


def read_bdf(path):
    valid_cards = [scl.__name__.upper() for scl in BulkDataEntry.__subclasses__()]
    with open(path) as f:
        # TODO figure out if there's a cleaner way to make f peekable.
        f = peekable(f)
        in_bulk = False
        for line in f:
            if not in_bulk:
                if line.strip().upper() == "BEGIN BULK":
                    in_bulk = True

            # Until case control cards are supported, elif below (instead of if) also skips all lines until BULK DATA
            # statement has been read.

            # skip blank lines and comments
            elif not line.strip() or line.strip().startswith("$"):
                pass
            else:
                card_image = line[:8].strip().upper()
                # Warn when unsupported card encountered
                if card_image not in valid_cards:
                    warnings.warn(f'Unsupported card image found: {card_image}')
                else:
                    field_data = read_card(line, f)
                    card = [scl(*field_data) for scl in BulkDataEntry.__subclasses__()
                            if scl.__name__.upper() == card_image][0]
        if not in_bulk:
            # BEGIN BULK is a required card for any valid Nastran job
            raise EOFError('No "BEGIN BULK" statement found.')


def read_card(line: str, f) -> list:
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
