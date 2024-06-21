import unittest
from naspy.BulkDataEntries import Cbar

fields = ('1558172', '31', '1115', '3903', '-1.0', '0.0', '0.0', '', '', '', '0.0', '0.0', '-3.0', '0.0', '0.0', '-3.0')
Cbar(*fields)


class TestCbarDependencies(unittest.TestCase):
    def test_pid(self):
        self.assertEqual(Cbar[1558172].dependencies['pid'], 31)

    def test_nodes(self):
        self.assertEqual(Cbar[1558172].dependencies['grid'], set([1115, 3903]))

    def test_seid(self):
        self.assertEqual(Cbar[1558172].dependencies['seid'], None)

if __name__ == '__main__':
    unittest.main()