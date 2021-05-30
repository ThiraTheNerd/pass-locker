import unittest
from user import User

class TestUser(unittest.TestCase):

  def setUp(self):
    self.user_account = User("user_name", "login_password")
  def test_init(self):
    self.assertEqual(self.user_account.login_name, "user_name")
    self.assertEqual(self.user_account.login_password, "login_password")

  def test_create_user(self):
    self.user_account.create_user()
    self.assertEqual(len(User.users_list), 1)

if __name__ == '__main__':
  unittest.main()