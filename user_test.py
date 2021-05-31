import unittest
from user import User

class TestUser(unittest.TestCase):

  def setUp(self):
    self.user_account = User("user_name", "login_password")
  def test_init(self):
    '''
    Tests the initialization function
    '''
    self.assertEqual(self.user_account.login_name, "user_name")
    self.assertEqual(self.user_account.login_password, "login_password")

  def test_save_user(self):
    '''
    Tests the save function
    '''
    self.user_account.save_user()
    self.assertEqual(len(User.users_list), 1)

  def test_verify_user(self):
    '''
    Tests the verify_user function
    '''
    self.user_account.save_user()
    account_exists = User.verify_login("user_name", "login_password")
    self.assertTrue(account_exists)

if __name__ == '__main__':
  unittest.main()