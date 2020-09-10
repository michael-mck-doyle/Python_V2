

# Tuple packing
t = 12345, 54321, 'hello!'
print(t)
# Tuple unpacking
x, y, z = t

print(x)
print(y)
print(z)




# examples taken (and adapted) from the linked docs

t = 12345, 54321, 'hello!'
print(t[0])
# 12345
print(t)
# (12345, 54321, 'hello!')

empty = ()
print(len(empty))
# 0
singleton = 'hello',  # <-- note trailing comma
print(len(singleton))
# 1
print(singleton)
# ('hello',)


berry1 = "python", "java", "c++"

print(berry1)
print(berry1[2])
print(berry1[0:2])


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup3 = tup1 + tup2
print(tup3)

