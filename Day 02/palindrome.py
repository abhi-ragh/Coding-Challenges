string = input("Enter A String: ").lower().replace(" ","")
print("The String is Palindrome") if string == string[::-1] else print("Not Palindrome")
