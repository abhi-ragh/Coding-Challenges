"""
Author: Abhiragh
Date: 25/08/2024
Description: Quiz Game
"""

questions ={
    "Who Discovered Gravity?\n1. Me\n2. You\n3. Newton\n4. Issak":3,
    "Which one of these is a Fruit?\n1. Cucumber\n2. Apple\n3. Chilli\n4. Pen":2,
    "Do You Like This Program?\n1. Yes\n2. Definitely\n3. Absolutely\n4. Ofcourse":1
}

# Add More Questions, Im Lazy :P

score = 0

for i in questions.keys():
    print(i)
    ans = int(input("Your Answer: "))
    if ans == questions[i]:
        score += 1
        print("Yay!!!\n")
    else:
        print("Nuhhh!!!\n")
        
print("Score: ",score)