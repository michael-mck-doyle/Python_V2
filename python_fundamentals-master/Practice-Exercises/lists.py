

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

'''
list.append(item)
list.remove(item)
list.sort()
del(list[index])
'''

stack = [3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

list1.append(list2)
print(list1)

list1.remove(list2)
print(list1)

list1.remove(list1[0])
print(list1)

list1.append('physics')
print(list1)

list1.reverse()
print(list1)


for i in list1:
    print(i)





# creating a list
bucket_list = ['climb Mt. Everest', 'eat fruits from a tree', 'raise a child']
print(bucket_list[0])  # this is how we can access individual items in the list

# let's see how lists are *mutable* by changing the second item
bucket_list[1] += ' that I planted'
print(bucket_list[1])

# ---- continuing the codeblock from above ---- #
# adding another list to the initial list
bucket_list += ['live in Barcelona', 'work at Google']

# notice that we are changing bucket_list *without re-assigning* the variable
# this is due to the fact that we are *mutating* the list in place
bucket_list.remove(bucket_list[-1])


for task in bucket_list:
    print(task)

