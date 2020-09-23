'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]
'''

list_1 = [1, 2, 6, 55, 2, 'hi', 'hi', 4, 2, 6, 1, 13, 6, 8, 9, 10, 10]
unique_list = []

for i in list_1:
    if i not in unique_list:
        unique_list.append(i)

print("List containing only unique value: ")
print(unique_list)


