'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
# take 10 numbers in from a user and enter into a list
num = 0
new_list = []
while num < 10:
    num_enter = int(input("Enter a number: "))
    new_list.append(num_enter)
    num = num + 1
print()
print("new_list = " + str(new_list))
print()

# Method 1 - use the 'range' function
print("Method 1 - uses range function")
print("the 'range' function syntax is range(start, stop, step)")
print("Details on the range function can be found here: https://www.w3schools.com/python/ref_func_range.asp")


for x in range(1, 11, 2):
    print ("Every second number in list is: " + str(new_list[x]))

print()
print()

for y in range(-2, -11, -2):
    print("Every second number in reverse is: " + str(new_list[y]))

print()
print("the list of numbers entered = " + str(new_list))
print()

# Method 2 - quite clumsy
print("Method 2 - clumsier method using while loop")
x = 1
y = 8
counter = 0
#new_list = [12, 24, 3, 10, 78, 16, 49, 47, 88, 100]




while counter < len(new_list)/2:
    print(new_list[x])
    x = x + 2
    counter = counter + 1

counter = 0

while counter < len(new_list)/2:
    print(new_list[y])
    y = y - 2
    counter = counter + 1

print("Done")
