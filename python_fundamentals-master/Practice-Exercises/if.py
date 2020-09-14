
number = int(input("Enter a number: "))

if number == 5:
    print("it's 5!")
elif number < 5:
    print("so low!")
elif number > 5 and number < 20:
    print("pretty decent.")
else:
    print("whoa slow down! so high, take care!")



'''
flag = input("Enter 'True' or 'False': ")
flag = bool(flag)
# if the condition evaluates to True, the indented code gets executed
# otherwise it is simply skipped
if flag == True:
    print("yay!")
else:
    print("woop!")


print(type(flag))


number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

'''
