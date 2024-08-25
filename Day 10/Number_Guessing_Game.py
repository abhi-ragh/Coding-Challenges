"""
Author: Abhiragh
Date: 25/08/2024
Description: Number Guessing Game
"""

import random

print("Number Guessing Game!!")
print("I Will Guess a Number Between 0 and 100, You Have to Guess it !!")

rand = random.randint(0,100)
guess = int(input("\nGuess the Number: "))

count = 0

while guess != rand:
    count += 1
    if guess < rand:
        print("Your Guess is Lesser")
    elif guess > rand:
        print("Your Guess is Greater")
    
    guess = int(input("\nGuess the Number: "))

print("You Guessed Correctly")
print("No of Attempts = ", count)