"""
Author: Abhiragh
Date: 16/09/2024
Description: Write a function that merges two sorted arrays into one sorted array.
"""

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range(1,len(array)):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                
    return array

array_1 = eval(input("Enter A List: "))
array_2 = eval(input("Enter Second List: "))

merged_array = array_1 + array_2
print(bubble_sort(merged_array))
