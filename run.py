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

def delete_account(account):
  Credentials.delete_account_credentials(account)

def verify_user(string):
  Credentials.verify_login(string)

def main():
  print("Hello, welcome to Password locker. Do you have an existing password locker account?\
     Type Yes of No")
  has_account = input().lower()

  if has_account == 'yes':
    print("Enter your Login Credentials")
    print("-"*20)
    print("Username")
    print("-"*10)
    user_name = input()
    print("Password")
    print("-"*10)
    pass_word = input()
    login_data = user_name + pass_word

    if verify_user(login_data):
      Print(f"You have successfully Logged into Password Locker")
    else :
      print("Data provided does not match any exsisting accounts.")
  else :
    print("Unrecognized input")
    









if __name__ == "__main__":
  main()
