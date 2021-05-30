class User():
  users_list = []
  def __init__(self,login_name,login_password, login_data):
    self.login_name = login_name
    self.login_password = login_password
    self.login_data = login_name + login_password

  def save_user(self):
    User.users_list.append(self)

  @classmethod
  def verify_login(cls,string):
    for user in cls.users_list:
      if user.login_data == string:
        return True
      return False
      