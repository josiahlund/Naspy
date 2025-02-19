import unittest
from naspy.cards import Cbar

fields = ('1558172', '31', '1115', '3903', '-1.0', '0.0', '0.0', '', '', '', '0.0', '0.0', '-3.0', '0.0', '0.0', '-3.0')
cbar = Cbar(*fields)


class TestCbarDependencies(unittest.TestCase):
    def test_pid(self):
        self.assertEqual(cbar.dependencies['pid'], 31)

    def test_nodes(self):
        self.assertEqual(cbar.dependencies['grid'], set([1115, 3903]))

    def test_seid(self):
        self.assertEqual(cbar.dependencies['seid'], None)

if __name__ == '__main__':
    unittest.main()