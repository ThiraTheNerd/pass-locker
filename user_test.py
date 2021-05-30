import unittest
from user import User

class TestUser(unittest.TestCase):

  def setUp(self):
    self.user_account = User("user_name", "login_password")
  def test_init(self):
    self.assertEqual(self.user_account.user_name, "user_name")
    self.assertEqual(self.user_account.login_password, "login_password")

if __name__ == '__main__':
  unittest.main()