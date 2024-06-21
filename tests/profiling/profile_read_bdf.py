import warnings
from profile_utils import profile_function
from naspy.SCRIPTS.read_bdf import read_bdf

# Suppress warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    # Specify the path to the file
    path = "C:/Users/Josiah/Documents/Projects/MSCNastranTools/naspy/sample_files/nug_29.dat"

    profile_function(read_bdf, path)
