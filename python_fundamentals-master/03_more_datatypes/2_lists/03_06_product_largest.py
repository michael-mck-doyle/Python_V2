'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))
num_4 = int(input("Enter a number: "))
num_5 = int(input("Enter a number: "))

num_list = [num_1, num_2, num_3, num_4, num_5]

max_num = max(num_list)
print(max_num)

x = 0

for i in num_list:
    x = x + i

print(x)

