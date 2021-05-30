import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
  def setUp(self):
    self.twitter_account = Credentials("twitter", "twitter_username", "twitter_pass")
  def test_init(self):
    self.assertEqual(self.twitter_account.account_name, "twitter")
    self.assertEqual(self.twitter_account.user_name, "twitter_username")
    self.assertEqual(self.twitter_account.password, "twitter_pass")
  def test_save_credentials(self):
    self.twitter_account.save_credentials()
    self.assertEqual(len(Credentials.user_accounts), 2)

  def test_display_credentials(self):
    self.assertEqual(Credentials.display_credentials(), Credentials.user_accounts)

  def test_delete_account_credentials(self):
    self.twitter_account.save_credentials()
    self.twitter_account.delete_account_credentials()
    self.assertEqual(len(Credentials.user_accounts), 0)

  def test_find_account(self):
    self.twitter_account.save_credentials()
    found_account = Credentials.find_account("twitter")
    self.assertEqual(found_account.user_name, "twitter_username")



if __name__ == "__main__":
  unittest.main()

