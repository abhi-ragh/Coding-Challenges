"""
Author: Abhiragh
Date: 25/08/2024
Description: Rock Paper Scissor Game
"""

import random

choices = ["Rock","Scissors","Paper"]

def Tie(comp_choice,user_choice):
    print(f"User: {choices[user_choice-1]}")
    print(f"Computer: {choices[comp_choice-1]}")
    print(f'''Tie!!''')
    
def Win(comp_choice,user_choice):
    print(f"User: {choices[user_choice-1]}")
    print(f"Computer: {choices[comp_choice-1]}")
    print(f'''Win!!''')
    
def Lose(comp_choice,user_choice):
    print(f"User: {choices[user_choice-1]}")
    print(f"Computer: {choices[comp_choice-1]}")
    print(f'''Lose!!''')

print("1. Rock\n2. Paper\n3. Scissors")
user_choice = int(input("Choose: "))
computer_choice = random.randint(1,3)

if computer_choice == 1:
    if user_choice == 1:
        Tie(computer_choice,user_choice)
    elif user_choice == 2:
        Lose(computer_choice,user_choice)
    elif user_choice == 3:
        Win(computer_choice,user_choice)

elif computer_choice == 2:
    if user_choice == 1:
        Win(computer_choice,user_choice)
    elif user_choice == 2:
        Tie(computer_choice,user_choice)
    elif user_choice == 3:
        Lose(computer_choice,user_choice)

elif computer_choice == 3:
    if user_choice == 1:
        Lose(computer_choice,user_choice)
    elif user_choice == 2:
        Win(computer_choice,user_choice)
    elif user_choice == 3:
        Tie(computer_choice,user_choice)

