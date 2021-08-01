import warnings


def read_bdf(path):
    valid_cards = []
    with open(path) as f:
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

        if not in_bulk:
            # BEGIN BULK is a required card for any valid Nastran job
            raise EOFError('No "BEGIN BULK" statement found.')
