'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = input("Please enter a sentence: ")

x = sentence.split(" ")


for i in sentence:
    sentence.strip(i)


# Hello, Hello, is anyone there? Is today a good day to say hello?
