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
    self.assertEqual(len(Credentials.user_accounts), 1)


if __name__ == "__main__":
  unittest.main()

