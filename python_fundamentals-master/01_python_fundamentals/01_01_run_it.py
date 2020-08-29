'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.
'''

print ("hello world!")

print (1 + 2)

x = 2 * 10
print(x)


# user input is *always* gathered as a string
# and needs to be converted if we want something else

age = input("Please enter your age: ")
print(type(age)) # checking up on current type

age = int(age)
print(type(age)) # successfully converted the user input to an integer

years = input("Choose a number between 1 - 10 years: ")
num_years = int(years)

seconds = num_years * 365 * 24 * 60 * 60

print("The number of seconds in " + years + " years is " + str(seconds) + " seconds")

print (type(years))
print(type(years))
