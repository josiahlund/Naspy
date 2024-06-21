import warnings
from profile_utils import profile_function
from naspy.SCRIPTS.read_bdf import read_card

# Suppress warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    # Specify the path to the file
    path = "C:/Users/Josiah/Documents/Projects/MSCNastranTools/naspy/sample_files/nug_29.dat"

    with open(path, "r") as f:
        for line in f:
            profile_function(read_card, line, f)
            break
