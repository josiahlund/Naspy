import unittest
from naspy.BulkDataEntries import Grid


class TestGridDependencies(unittest.TestCase):

    def test_pid(self):
        Grid('2', '', '1431.033', '436.7573', '170.9705', '', '', '')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_nodes(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_seid(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()