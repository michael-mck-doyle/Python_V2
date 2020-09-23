'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 3, 3, 4], [5, 3, 6], [7, 3, 8, 9]]
flattened_list_unique = []
flattened_list_all = []

# Solution uses a nested for loop to
for i in starting_list:
    for y in i:
        if y not in flattened_list_unique:
            flattened_list_unique.append(y)

for i in starting_list:
    for y in i:
        flattened_list_all.append(y)

print("Flattened list with unique values: " + str(flattened_list_unique))
print("Flattened list containing all values: " + str(flattened_list_all))

