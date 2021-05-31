class User():
  users_list = []
  def __init__(self,login_name,login_password):
    self.login_name = login_name
    self.login_password = login_password
  def create_user(self):
    '''
    Function to create a new user
    '''
    new_user = User(login_name, login_password)

  def save_user(self):
    User.users_list.append(self)

  @classmethod
  def display_users(cls):
    return cls.users_list

  @classmethod
  def verify_login(cls,logname,login_pass):
    for user in cls.users_list:
      if (user.login_name == logname and user.login_password == login_pass):
        return True
      return False
