# import the random and string packages to help generate passwords

import random
import string

# Asks the user for the length of their desired password
passLength = int(input("Welcome to my password generator! \n"
                       "Please enter the length of the desired password: "))

# Collects all potential data to be used in password generation
collectedData = string.ascii_letters + string.digits + string.punctuation

# Generates the password
tempPass = random.sample(collectedData, passLength)
password = "".join(tempPass)

# Displays the generated password
print("The generated password is:", password)
