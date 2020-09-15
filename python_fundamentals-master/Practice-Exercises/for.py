


# As an exercise, write a function that takes a string as an argument and displays the letters backward, one per line.


word = input("Please enter a word: ")

x = 0


while x < len(word):
    i = 1
    print(word[len(word) - i])

    i = i + 1
    x = x + 1



'''
users = {'mary': 22, 'caroline': 26, 'harry': 20}
# let's make them age for 30 years each!

for user, age in users.items():
    aged = age + 30
    print(user, aged)
'''
'''
my_list = [1, 2, 3, "hello", "it's blue!", 10]

for i in my_list:
    print(i)
'''

