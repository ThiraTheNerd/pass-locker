class User():
  users_list = []
  def __init__(self,login_name,login_password):
    self.login_name = login_name
    self.login_password = login_password

  def save_user(self):
    User.users_list.append(self)