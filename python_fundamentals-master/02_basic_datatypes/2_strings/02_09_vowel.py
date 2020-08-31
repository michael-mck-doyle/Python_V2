'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''


user_string = input("Please enter a short sentence: ")
user_letter = input("Please enter one letter: ")

x = user_string.count(user_letter)
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
print(x)

a = user_string.count(a)
e = user_string.count(e)
i = user_string.count(i)
o = user_string.count(o)
u = user_string.count(u)

print("The number of vowels respectively starting at 'a' is: "); print(a, e, i, o, u)

