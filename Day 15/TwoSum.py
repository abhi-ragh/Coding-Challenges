"""
Author: Abhiragh
Date: 10/09/2024
Description: Write a function that takes an array of integers and a target sum. The function should return True if any two numbers in the array add up to the target sum, and False otherwise.
"""

def twosum(arr, target):
    for i in arr:
        for j in arr:
            if int(i)+int(j) == target:
                return True
    return False

arr = list(input("Enter An Array of Numbers: "))
target = int(input("Enter Target Sum: "))
print(arr)
print(twosum(arr,target))
