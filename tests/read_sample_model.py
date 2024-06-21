from naspy.SCRIPTS import read_bdf


def main():
    db_dict = read_bdf("../naspy/sample_files/nug_29.dat")
    return db_dict


if __name__ == "__main__":
    main()
