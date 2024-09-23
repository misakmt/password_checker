#!/opt/homebrew/bin/python3

import sys

# Take user input
def user_input():
    valid = False
    while (valid == False):
        user_password = input("Please enter a password to check its strength: ")
        print(f"Password entered: {user_password}")

        # run it
        if (valid_password_check(user_password) == True):
            scoring_system(user_password)
            break
        else:
            valid = False
            
# Check to make sure password contains at least 1 uppercase letter, a number, and special character
def valid_password_check(user_password):
    has_upper = False
    has_digit = False
    has_special_character = False
    has_above12_char = False

    for char in user_password:
        if (char.isupper()):
            has_upper = True
        elif (char.isdigit()):
            has_digit = True
        elif not (char.isalnum()):
            has_special_character = True
        elif (len(user_password) >= 12):
            has_above12_char = True
            
    if (has_upper and has_digit and has_special_character and has_above12_char):
        valid = True
    else:
        valid = False
        print ("Password is weak. Does not contain at least 12 characters, an uppercase letter, number, and/or special character. \n")

    return valid

# Scoring System
def scoring_system(user_password):
    # empty print for readability
    print("")
    character_count = len(user_password)
    print (f"characters: {character_count}")

    # count of uppercase letters
    uppercase_count = sum(1 for char in user_password if char.isupper())
    print (f"uppercase count: {uppercase_count}")

    # count of numbers
    number_count = sum (1 for char in user_password if char.isdigit())
    print (f"number count: {number_count}")

    # count of special characters (non alphanumeric)
    special_char_count = sum(1 for char in user_password if not char.isalnum())
    print (f"special character count: {special_char_count}")

user_input()
sys.exit(0)