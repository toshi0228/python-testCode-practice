import unittest
from user import User


class TestUser(unittest.TestCase):

    def test_fullname(self):
        user = User('佐藤', '二郎', "")
        actual = user.fullname()
        self.assertEqual(actual, "佐藤二郎")

    def test_role_staff(self):
        user = User("", "", "eee@gmail.com")
        actual = user.role()
        self.assertEqual(actual, "staff")

    def test_role_viewer(self):
        user = User('', '', 'eee@gmheail.com')
        actual = user.role()
        self.assertEqual(actual, 'viewer')
