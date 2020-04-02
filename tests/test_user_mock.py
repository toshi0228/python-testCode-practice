import unittest
from unittest import mock
from user_mock import get_username, get_sign


class TestGetUsername(unittest.TestCase):

    def test__get(self):
        dummy_user = mock.Mock()
        dummy_user.username = 'john'
        print(dummy_user)
        self.assertEqual(get_username(dummy_user), 'john')


class TestGetSign(unittest.TestCase):

    def test__get(self):
        dummy_user = mock.Mock()
        dummy_user.get_fullname.return_value = 'toshi'
        dummy_user.email = 'etoshi@example.com'
        self.assertEqual(get_sign(dummy_user), 'toshi')
        dummy_user.get_fullname.assert_called_with()


# class TestGetSign(unittest.TestCase):
#     def test__get(self):
#         dummy_user = mock.Mock()
#         dummy_user.get_fullname.return_value = 'John Doe'
#         dummy_user.email = 'john@example.com'

#         self.assertEqual(get_sign(dummy_user),
#                          'John Doe <john@example.com>')
#         dummy_user.get_fullname.assert_called_with()
