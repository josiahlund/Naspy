import warnings
from BulkDataEntries import registry
from more_itertools import peekable
import tkinter as tk
from tkinter import filedialog


def read_bdf(path: str) -> object:
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
                    break
        if not in_bulk:
            # BEGIN BULK is a required card for any valid Nastran job
            raise EOFError('No "BEGIN BULK" statement found.')
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
                if (ID := int(field_data[0])) in bulk_data[card_image]:
                    warnings.warn(f'Duplicate {card_image} entry with ID {ID}')
                    print(bulk_data[card_image][ID])
                    print(card)
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
            line = f.peek()
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
            else:
                next(f)
    return tuple(card_data)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfile()
    read_bdf(file.name)
