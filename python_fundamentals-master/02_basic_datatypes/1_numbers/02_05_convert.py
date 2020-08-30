'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# Convert an int to a float

x = 2
x = 2 / 4
print(x)


# Convert a float to an int

x = 2.5
x = int(2.5)
print(x)


# Perform floor division using a float and an int

x = 4.6 // 2
print(x)

x = 2//4.6
print(x)


# Use two user inputted values to perform multiplication

user1 = (int(input("Please enter any number: ")))
user2 = (int(input("Please enter any number: ")))

print(user1 * user2)
