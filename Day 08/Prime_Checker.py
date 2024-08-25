"""
Author: Abhiragh
Date: 24/08/2024
Description: Prime Checker
"""

num = int(input("Enter A Number: "))
flag = True
for i in range(2,num):
    if num%i == 0:
        flag = False
print("Prime") if flag == True else print("Not Prime")