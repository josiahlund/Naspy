import pytest
from naspy.SCRIPTS import read_bdf


@pytest.mark.benchmark
def test_read_bdf(benchmark):
    path = "C:/Users/Josiah/Documents/Projects/MSCNastranTools/naspy/sample_files/nug_29.dat"
    benchmark(read_bdf, path)
