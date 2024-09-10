"""
Author: Abhiragh
Date: 10/09/2024
Description: Write a function that takes an array of integers and moves all the zeros to the end while maintaining the relative order of the other elements.
"""

def move(arr):
    for i in arr:
        if i=='0':
            arr.remove(i)
            arr.append('0')
    return arr

arr = list(input("Enter Array of Integers: "))
print(move(arr))
