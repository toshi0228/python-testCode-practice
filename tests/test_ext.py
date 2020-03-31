import unittest

from ext import find_extension


class TestFindExtension(unittest.TestCase):
    def test_existed(self):
        actual = find_extension('/path/to/main.py')
        self.assertEqual(actual, 'python')

    def test_not_exit(self):
        actual = find_extension('/path/to/some.note')
        self.assertEqual(actual, 'NONE')
