'''

Write a script that removes all duplicates from a list.

'''

new_list = [1, 2, 3, 4, 3, 4, 5, 3, 'multiple', 'multiple']

# Method 1 - use loops and if statement to remove duplicates
print("Method 1 - use loops and if statement")
dup_list = []
single_list = []

for i in new_list:
    if i not in single_list:
        single_list.append(i)
    else:
        print(str(i) + " is a duplicate")
        dup_list.append(i)

print("List with no duplicates: " + str(single_list))
print("List of duplicates: " + str(dup_list))

# Method 2 - use remove command
new_list_dups = [1, 2, 3, 4, 3, 4, 5, 3]
print()
print()
print("Method 2 - using count and remove functions")
for i in new_list:
    if new_list_dups.count(i) > 1:
        new_list_dups.remove(i)

print(new_list_dups)

# Method 3 - easier than Method 1 change the list into a set since sets cannot contain duplicates.
# You can then change the set back into a list
print()
print("Method 3 - use sets to remove duplicates in a list")
new_set = set(new_list)
print("Set has no duplicates: " + str(new_set))
new_list2 = list(new_set)
print("A list derived from a set contains no duplicates: " + str(new_list2))




