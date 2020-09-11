

users = {'mary': 22, 'caroline': 26, 'harry': 22}
print(users['mary']) # using the key to return the value of key 'mary'

users['harry'] = 20 # changing the original value of 'harry'
print(users['harry'])

for user, age in users.items():
    print(user, age)

for user, age in users.items():
    age = age + 10
    print(user, age)

for k in users.keys(): # returns just the keys
    print(k)

for v in users.values(): # returns just the values
    print(v)


dict_to_list = list(users) # converts a dictionary to a list
print(dict_to_list)
dict_to_tuple = tuple(users) # converts a dictionary to a tuple
print(dict_to_tuple)
dict_to_set = set(users) # converts a dictionary to a tuple
print(dict_to_set)

cars = {'Honda': 22, "Toyota": 15, " Suzuki": 7, "BMW": 12}

cars2 = cars.copy()
print(cars2)

cars2.clear()
print(cars2)

cars3 = cars.fromkeys('Sazuki', "Honda")
print(cars3)

print(cars.get('Honda'))

cars.update({'Honda': 27, 'Mazda' : 32})
print(cars)

