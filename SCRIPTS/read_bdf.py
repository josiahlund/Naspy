import warnings
from BulkDataEntries import registry
import tkinter as tk
from tkinter import filedialog


def read_bdf(path: str) -> object:
    with open(path) as f:
        # If there is a "BEGIN BULK" statement anywhere within the file being read, assume the file also contains pre-
        # bulk entries (Nastran statments, executive control, file management statements, case control statements) which
        # are not yet supported and are skipped.
        if "BEGIN BULK" in f.read():
            in_bulk = False
        else:
            in_bulk = True

        # Rewind to beginning of file and begin reading line by line
        f.seek(0)
        for line in f:
            while not in_bulk:
                # Until case control cards are supported, skip all lines until BEGIN BULK statement has been read.
                if line.strip().upper() == "BEGIN BULK":
                    in_bulk = True
                line = next(f)
            bulk_data_entries = read_bulk_data(f)
            break
    return bulk_data_entries


def read_bulk_data(f: object) -> dict:
    valid_cards = registry.keys()
    bulk_data = {card: {} for card in valid_cards}
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
                card = registry[card_image](*field_data)
                # Check if entry already exists to prevent overwriting data (LBYL)
                if (ID := int(field_data[0])) in bulk_data[card_image]:
                    # If this card already exists but with different fields, raise a warning
                    if repr(bulk_data[card_image][ID]) != repr(card):
                        # TODO: add decorator or event handler to log all errors/warnings for the entire BDF, so a
                        #       maximum number of issues can be identified with each use.
                        # TODO: add detail to warning message to inform what field(s) have differences
                        warnings.warn(f'Duplicate {card_image} entry of ID {ID} with difference in one or more fields')
                        print(bulk_data[card_image][ID])
                        print(card)
                    else:
                        # data is identical to the data which has already been read, no need to read again.
                        pass
                else:
                    bulk_data[card_image][ID] = card
    return bulk_data


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
            line = next(f)
        except StopIteration:
            # EOF
            break
        else:
            # If line is empty or a comment, break
            if not line.strip() or line.strip().startswith("$"):
                break
            # If line is not a continuation, break
            elif not any(line[:8].startswith(c) for c in ["+", "*", " "]):
                break
    return tuple(card_data)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfile()
    read_bdf(file.name)
