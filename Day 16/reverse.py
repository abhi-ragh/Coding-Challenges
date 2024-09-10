"""
Author: Abhiragh
Date: 10/09/2024
Description: Write a function that takes a string as input and returns the string with the words reversed.
"""

def reverse(strr):
    strr = strr.split(" ")
    strr =  strr[::-1]
    return " ".join(strr)

strr = input("Enter A String: ")
print(reverse(strr))
