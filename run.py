#!/usr/bin/python3.8

from user import User
from credentials import Credentials
import pyperclip

def function():
	print("               ____      __        ____     ____         __           ____      _____   _    __             ")
	print("              |  _ \    /  \      / ___|   / ____|      |  |       /     \   /  _____| | |  / /          ")
	print("              | |_) )  / __ \    / /___   / /____       |  |      |       | |  |       | | / /             ")
	print("              |  __/  / |__| \   \____  \ \____ \       |  |      |  |_|  | |  |       | | \ \            ")
	print("              | |    /   __   \   ____| |  ____| |      |  |_____ |       | |  |_____  | |  \ \           ")
	print("              |_|   /___|  |___\ |_____ / |______/      |________| \_____/   \______ | |_|   \_\       ")
function()

def create_user(login_name, login_password):
  '''
  Creates an instance of the object user
  '''
  new_user = User(login_name, login_password)
  return new_user

def save_user(user):
  '''
  Saves an instance of a User
  '''
  User.save_user(user)

def create_account(account_name, user_name, password ):
  '''
  Creates the instance of a Credentials object
  '''
  new_account = Credentials(account_name, user_name, password)
  return new_account

def save_account(account):
  '''
  Saves the instance created
  '''
  Credentials.save_credentials(account)

def display_credentials():
  '''
  Displays a list of all saved accounts
  '''
  return Credentials.display_credentials()
def display_users():
  '''
  Displays a list of all saved users
  '''
  return User.display_users()

def delete_account(account):
  '''
  Deletes a specific account
  '''
  Credentials.delete_account_credentials(account)

def verify_user(login_name,login_pass):
  '''
  Confirm if user exists
  '''
  return User.verify_login(login_name,login_pass)

def find_account(string):
  '''
  LOoks for a specific account in the stored accounts
  '''
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
    print("-"*80)
    print(f"Hello {login_name} your account has been created successfully. Your new password is {login_pass}")
  while True:
    print("Use these short codes :\
      lg - To Login once again\
      cc - Add new account credentials,\
      dc - display all credentials,\
      fc - find account\
      gp - generate a random password\
      c  - To copy a string to the clipboard \
      p  - To paste whaterver is copied in the clipboard\
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
          pass_word = input("Password: ")
          break
        elif pass_type == "gp":
          print("\n")
          print("Enter desired password length")
          print("\n")
          string_length = int(input("Password Length: "))
          pass_word = generate_password(string_length)
          print("\n")
          break
        else:
          print("\n")
          print("Invalid password")
          print("\n")
          break
      save_account(create_account(acc_name,user_name,pass_word))
      print("\n")
      print(f"Account Credential for: {acc_name} - UserName: {user_name} - Password:{pass_word} created succesfully")
      print("\n")
    elif short_code ==  "lg":
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
          print("\n")
          break
        else :
          print("Data provided does not match any exsisting accounts.")
          print("\n")
          break

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
        print("\n")
    elif short_code == "fc":
      print("Enter the account name")
      account = input()
      found_account= find_account(account)
      print("\n")
      print(f"{found_account.account_name}, {found_account.user_name}, {found_account.password}")
      print("\n")

    elif short_code == "gp":
      print("Enter your desired password length")
      print("\n")
      string_length = int(input("Password Length : "))
      print("\n")
      pass_word = generate_password(string_length)
      print("\n")
      print(f"Your generated password is {pass_word}")
      print("\n")

    elif short_code == "c":
      print("What text would you like to copy to clipboard?")
      string_to_copy = input()
      copy_string = pyperclip.copy(string_to_copy)
      print("\n")
      print("Your Text has been copied to clip-board")
      print("\n")

    elif short_code == "p":
      while True:
        if copy_string != 0 :
          print(pyperclip.paste())
          break
        else:
          print("\n")
          print("Nothing has been copied to clip board")
          print("\n")

    elif short_code == "del":
      print("Which account would you like to delete?")
      print("\n")
      del_account = input("Enter the account name ie. Instagram : ")
      delete_account(find_account(del_account))
      print("\n")
      print(f"{del_account} has been deleted successfully")
      print("\n")
    elif short_code == 'ex':
      print("Bye...Thank you for using Pass Locker")
      break
    else:
      print("I really did not get that. Kindly use the short-codes")
  



if __name__ == "__main__":
  main()
