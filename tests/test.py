import unittest


def plus(a, b):
    return a + b


class TestPlus(unittest.TestCase):

    def test_Plus(self):
        self.assertEqual(10, plus(2, 8))


# python -m unittest discover tests/

# find_extension
