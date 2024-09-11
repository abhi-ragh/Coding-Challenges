"""
Author: Abhiragh
Date: 11/09/2024
Description: Write a function that checks if a string of parentheses is valid.
"""

def check(n) -> bool:
    d = { ")":"(","}":"{","]":"[" }
    stack = []

    for i in n:
        if i in d:
            top = stack.pop() if stack else '#'

            if d[i] != top:
                return False
        
        else:
            stack.append(i)

    return not stack

n = input("Enter String: ")
print(check(n))
