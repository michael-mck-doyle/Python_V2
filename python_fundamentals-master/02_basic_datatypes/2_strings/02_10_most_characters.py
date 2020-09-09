'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

user_string1 = input("Please enter a word: ")
user_string2 = input("Please enter a word: ")
user_string3 = input("Please enter a word: ")

user_string = [user_string1, user_string2, user_string3]

for i in user_string:
    print(i), print(len(i))



x = len(user_string1)
#print(x, user_string1)
y = len(user_string2)
#print(y, user_string2)
z = len(user_string1)
#print(z, user_string3)

string_lengths = [x, y, z]

print(string_lengths)

print(min(string_lengths))




