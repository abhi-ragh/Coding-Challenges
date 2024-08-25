"""
Author: Abhiragh
Date: 25/08/2024
Description: Password Generator
"""

import random
import string

length = int(input("Enter Password Length: "))
password_pool = []
password = ""
check = input("Include Lowercase Letter?(Y/N): ")
if check == "y" or check == "Y":
    password_pool += string.ascii_lowercase

check = input("Include Uppercase Letter?(Y/N): ")
if check == "y" or check == "Y":
    password_pool += string.ascii_uppercase

check = input("Include Digits?(Y/N): ")
if check == "y" or check == "Y":
    password_pool += string.digits

check = input("Include Special Symbols?(Y/N): ")
if check == "y" or check == "Y":
    password_pool += string.punctuation
    
if password_pool:
    for i in range(length):
        password += random.choice(password_pool)
    print("Your PassWord: ",password)
else:
    print("Choose atleast one option!!")