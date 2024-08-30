"""
Author: Abhiragh
Date: 30/08/2024
Description: Markup Parse
"""

n = int(input("Enter No of lines: "))
markup_list = []
list_started = False
for i in range(n):
    markup_input = input("Enter A Markup: ")
    markup_list.append(markup_input)


print("\nOutput: \n")
for i in markup_list:
    if i[0] == "#":
        if list_started:
            list_started = False
            print("</ul>")
        if i[1] == "#":
            print(f"<h2>{i[2:]}</h2>")
        else:
            print(f"<h1>{i[1:]}</h1>")
    elif i[0] == "*":
        if list_started:
            list_started = False
            print("</ul>")
        if i[1] == "*":
            print(f"<b>{i[2:len(i)-2]}</b>")
        else:
            print(f"<i>{i[1:len(i)-1]}</i>")
    elif i[0] == "-":
        if list_started:
            print(f"<li>{i[1:]}</li>")
        else:
            print(f"<ul>\n<li>{i[1:]}</li>")
            list_started = True
if list_started:
            list_started = False
            print("</ul>")