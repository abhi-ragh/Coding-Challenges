"""
Author: Abhiragh
Date: 16/09/2024
Description: Write a function that removes duplicates from a sorted array in place and returns the length of the array after duplicates are removed.
"""

def remove(array):
    for i in range(0,len(array)):
        try:
            while array[i]==array[i+1]:
                array.remove(array[i])
        except:
            return len(array)

array = eval(input("Enter A Sorted List: "))
print(remove(array))
