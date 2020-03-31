import unittest


def plus(a, b):
    return a + b


class TestPlus(unittest.TestCase):

    def test_Plus(self):
        self.assertEqual(10, plus(2, 8))


# python -m unittest discover tests/

    # def test_with_key(self):
    #     """ key="code" を指定して code の値をキーにする場合
    #     """
    #     actual = list_to_dict(
    #         [{'code': 'Val', 'name': 'ロッシ'},
    #          {'code': 'Mar', 'name': 'マルケス'},
    #          {'code': 'Lor', 'name': 'ロレンソ'}],
    #         key='code'
    #     )
    #     self.assertEqual(actual, {
    #         'Val': {'code': 'Val', 'name': 'ロッシ'},
    #         'Mar': {'code': 'Mar', 'name': 'マルケス'},
    #         'Lor': {'code': 'Lor', 'name': 'ロレンソ'},
    #     })
