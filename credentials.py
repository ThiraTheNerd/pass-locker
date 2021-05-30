class Credentials():

  user_accounts= []
  def __init__(self,account_name,user_name,password):
    self.account_name = account_name
    self.user_name = user_name
    self.password = password

  def save_credentials(self):
    Credentials.user_accounts.append(self)

  @classmethod
  def display_credentials(cls):
    return cls.user_accounts

  def delete_account_credentials(self):
    Credentials.user_accounts.remove(self)

  @classmethod
  def find_account(cls,string):
    for account in cls.user_accounts:
      if account.account_name == string:
        return account

  





































    


