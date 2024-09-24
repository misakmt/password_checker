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
            # Gather counts and score by getting returned values from passwd_character_count function
            # Run the following functions
            character_count, uppercase_count, number_count, special_char_count = passwd_character_count(user_password)
            scoring_system(character_count, uppercase_count, number_count, special_char_count)
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
        print ("")
        print ("Error: Password is weak! Does not contain at least 12 characters, an uppercase letter, number, and/or special character. \n")

    return valid

# Get password details
def passwd_character_count(user_password):
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
    print (f"special character count: {special_char_count} \n")

    return character_count, uppercase_count, number_count, special_char_count

# Scoring System
def scoring_system(character_count, uppercase_count, number_count, special_char_count):
    score = 0
    # Length score
    if (character_count >= 12 and character_count <= 14):
        score += 1
    elif (character_count >= 15 and character_count <= 17):
        score += 2
    elif (character_count >= 18 and character_count <= 20):
        score += 3
    elif (character_count >= 21 and character_count <= 24):
        score += 4
    else:
        score += 5

    # Uppercase Score
    score += min(uppercase_count, 4) # take minimum value, but cap at 4

    # Digit Score
    score += min(number_count, 4) # take minimum value, but cap at 4

    # Special Character Score
    score += min(special_char_count, 5) # take minimum value, but cap at 5

    print(f"Password Score: {score}")

    if score <= 5:
        print("Weak password. Consider adding more characters, numbers, and special characters.")
    elif score <= 8:
        print("Okay password. Could be better.")
    elif score <= 10:
        print("Good password. Nice mix of characters.")
    elif score <= 12:
        print("Strong password. Well done!")
    else:
        print("Very strong password!")

# Run the first function to kickstart everything else
user_input()

sys.exit(0)