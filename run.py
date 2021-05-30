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
  User.verify_login(string)

def find_account(string):
  Credentials.find_account(string)

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
      Print(f"You have successfully Logged into Password Locker. You can view all your accounts below")
      display_credentials()

    else :
      print("Data provided does not match any exsisting accounts.")

  elif has_account == "no":
    print("CREATE NEW ACCOUNT")
    print("Please enter your desired username and Password for your password locker account.")
    print("-"*20)
    print("Username")
    print("-"*10)
    login_name = input()
    print("Password")
    print("-"*10)
    login_pass = input()

    save_user(create_user(login_name,login_pass))
    print("Account has been created successfully")

  else :
    print("Unrecognized input")

  print("What action would you like to perform? ")
  print("Use these short codes : cc - create a new account credentials, dc - display all credentials,\n"
     "del - Delete a credential account, ex -exit the contact list ")
  short_code = input().lower()

  if short_code == "cc":
    print("What account would you like to save credentials for?")
    print("Account Name")
    acc_name = input()
    print("Enter desired user_name")
    user_name = input()

    print("Enter desired password")
    pass_word = input()

    save_account(create_account(acc_name,user_name,pass_word))
    print("Account has beed added to your credentials list")

  elif short_code == "dc":
    if display_credentials():
      Print("Here is a list of all your account credentials")

      for account in display_credentials():
        print(f"{Credentials.account_name} -- {credentials.user_name} -- {Credentials.password} ")
        print("\n")

    else:
      print("You have not saved any account credentials")

  elif short_code == "del":
    print("Which account would you like to delete?")
    del_account = input("Enter the account name ie. Instagram")
    delete_account(find_account(del_account))
    print(f"{del_account} has been deleted successfully")
    



if __name__ == "__main__":
  main()
