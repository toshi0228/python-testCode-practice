import unittest
from converter import list_to_dict


class TestListToDict(unittest.TestCase):

    def test_default_key(self):
        actual = list_to_dict(
            [
                {'id': 1, 'name': 'あああ'},
                {'id': 2, 'name': 'いいい'}
            ],
        )
        self.assertEqual(actual, {
            1: {"id": 1, 'name': 'あああ'},
            2: {"id": 2, 'name': 'いいい'}
        })

    def test_with_key(self):
        '''key="code"を指定してcodeの値をキーに指定
        '''

        actual = list_to_dict(
            [{'code':  'Val', 'name': 'ううう'},
             {'code':  'Mar', 'name': 'えええ'}],
            key='code'
        )
        self.assertEqual(actual, {
            'Val': {'code':  'Val', 'name': 'ううう'},
            'Mar': {'code':  'Mar', 'name': 'えええ'},
        })

    def test_duplicate_key(self):
        """key="code"を指定して、codeの値をキーにする場合
        """

        actual = list_to_dict(
            [{"id": 1, "name": "フシギダネ"},
             {"id": 2, "name": "フシギソウ"},
             {"id": 2, "name": "フシギバナ"}
             ]
        )
        self.assertEqual(actual, {
            1: {'id': 1, 'name': 'フシギダネ'},
            2: {'id': 2, "name": "フシギバナ"}
        })

    # def test_duplicate_key(self):
    #     """ キーに重複がある場合のテスト
    #     """
    #     actual = list_to_dict(
    #         [{'id': 1, 'name': 'ロッシ'},
    #          {'id': 2, 'name': 'マルケス'},
    #          {'id': 2, 'name': 'ロレンソ'}],
    #     )
    #     self.assertEqual(actual, {
    #         1: {'id': 1, 'name': 'ロッシ'},
    #         2: {'id': 2, 'name': 'ロレンソ'},
    #     })

# python -m unittest discover tests/
