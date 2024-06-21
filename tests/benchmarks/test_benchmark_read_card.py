import pytest
from naspy.SCRIPTS.read_bdf import read_card


@pytest.mark.benchmark
def test_read_card(benchmark):
    path = "C:/Users/Josiah/Documents/Projects/MSCNastranTools/naspy/sample_files/nug_29.dat"

    with open(path, "r") as f:
        for line in f:
            benchmark(read_card, line, f)
            break
