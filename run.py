#!/usr/bin/python3.8

from user import User
from credentials import Credentials

def create_user(login_name, login_password):
  new_user = User(login_name, login_password)
  return new_user

def save_user(user):
  User.save_user(user)

def create_account(account_name, user_name, password ):
  new_account = Credentials(account_name, user_name, password)
  return new_account

def save_account(account):
  Credentials.save_credentials(account)

def display_credentials():
  return Credentials.display_credentials()
def display_users():
  return User.display_users()

def delete_account(account):
  Credentials.delete_account_credentials(account)

def verify_user(login_name,login_pass):
  '''
  Confirm if user exists
  '''
  return User.verify_login(login_name,login_pass)

def find_account(string):
  return Credentials.find_account(string)

def generate_password(number):
  '''
  Generates a random password
  '''
  auto_password = Credentials.generate_password(number)
  return auto_password


def main():
  print("Hello Welcome to your accounts password store.")
  print("Do you have an excisting account? Type yes or no")
  has_account = input().lower()
  if has_account == "yes":
    print("Enter your Login Credentials")
    print("-"*20)
    print("Username")
    print("T-"*10)
    logname = input("Username: ")
    print("password: ")
    print("-"*10)
    pass_word = input()
    while True:

      if verify_user(logname, pass_word):
        print("You have successfully Logged into Password Locker.")
        break
      else :
        print("Data provided does not match any exsisting accounts.")
        break
    

  elif has_account == "no":
    print("CREATE NEW ACCOUNT")
    print("Please enter your desired username and Password for your password locker account.")
    print("-"*20)
    print("Username")
    print("="*10)
    login_name = input()
    print("Password")
    print("-"*10)
    login_pass = input()

    save_user(create_user(login_name,login_pass))
    print("Account has been created successfully")
  #   print("You can now log into your account")
    print("-"*80)
    print(f"Hello {login_name} your account has been created successfully. Your new password is {login_pass}")
  while True:
    print("Use these short codes :\
      cc - Add new account credentials,\
      dc - display all credentials,\
      fc - find account\
      gp - generate a random password\
      del - Delete a credential account,\
      ex -exit ")
    short_code = input().lower()

    if short_code == "cc":
      # isLoggedIn()
      print("What account would you like to save credentials for?")
      print("Account Name")
      acc_name = input()
      print("Enter desired user_name")
      user_name = input()
      print("\n")
      print("Please type cp - to enter your own password and \
        gp- to generate a random password write ")
      print("\n")
      pass_type = input().lower()
      while True:
        if pass_type == "cp":
          pass_word = input("Password: ").isnumeric()
          break
        elif pass_type == "gp":
          print("\n")
          print("Enter desired password length")
          string_length = int(input("Password Length: "))
          pass_word = generate_password(string_length)
          break
        else:
          print("\n")
          print("Invalid password")
          break
      save_account(create_account(acc_name,user_name,pass_word))
      print("\n")
      print(f"Account Credential for: {acc_name} - UserName: {user_name} - Password:{pass_word} created succesfully")
      print("\n")
    elif short_code == "dc":
      if display_credentials():
        print("Here is a list of all your account credentials")
        print("\n")

        for account in display_credentials():
          print(f"{account.account_name} -- {account.user_name} -- {account.password} ")
          print("\n")

      else:
        print("\n")
        print("You have not saved any account credentials")
    elif short_code == "fc":
      print("Enter the account name")
      account = input()
      found_account= find_account(account)
      print("\n")
      print(f"{found_account.account_name}, {found_account.user_name}, {found_account.password}")


    elif short_code == "del":
      print("Which account would you like to delete?")
      print("\n")
      del_account = input("Enter the account name ie. Instagram")
      delete_account(find_account(del_account))
      print("\n")
      print(f"{del_account} has been deleted successfully")
  



if __name__ == "__main__":
  main()
