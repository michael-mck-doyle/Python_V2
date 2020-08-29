'''

Move the code you previously wrote to calculate how many seconds are in a year into this file.
Then execute it as a script to see the output printed to your console.

'''
years = input("Choose a number between 1 - 10 years: ")
num_years = int(years)

seconds = num_years * 365 * 24 * 60 * 60

print("The number of seconds in " + years + " years is " + str(seconds) + " seconds")

print (type(years))
print(type(years))


fruit = "banana"
fruity = fruit[2:]
print (fruity)
fruit = fruity.capitalize()
print(fruit)


name = "Albert Smith"
surname = " Einstein"
name = name[0:6] + surname
print(name)

