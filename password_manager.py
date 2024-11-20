#!/opt/homebrew/bin/python3

import sys
import getpass

def user_options():
    print("Choose an option: ")
    print("1: log in")
    print("2: go back to main menu")
    print("99: Exit")

    choice = input("\n")

    if (choice == "1"):
        # Case 1 - Password Strength Check
        login()
        user_options()

    elif (choice == "2"):
        # Case 2 - Generate Random Password
        from password_check import main
        main()
        # print("work in progress")

    elif (choice == "99"):
        print("Exiting! \n")
        sys.exit(0)

def login():
    # print ("hello \n")
    user_email = input("Enter username/email: ")
    user_pwd = getpass.getpass("Enter password: ")



# NOTES:

# Store password in an encrypted file and make sure password is also encrypted - in the future, this could be a hidden and encrypted directory
# make different folder for different usernames -- if entered username is not found, ask user if they want to create a new entry and prompt them for a password

# Asymmetrical encryption --> each vault has it's own public key in the directory (of course hidden) and only the owner of the vault can unlock
# it using their very own private key or better yet, the passphrase to the private key

