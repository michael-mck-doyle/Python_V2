'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

user_string = input("Please enter a short sentence: ")
user_letter = input("Please enter one letter: ")

x = user_string.find(user_letter)

print(x)
