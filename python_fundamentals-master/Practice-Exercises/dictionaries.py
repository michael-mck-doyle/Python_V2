

users = {'mary': 22, 'caroline': 26, 'harry': 22}
print(users['mary']) # using the key to return the value of key 'mary'

users['harry'] = 20 # changing the original value of 'harry'
print(users['harry'])

for user, age in users.items():
    print(user, age)

for user, age in users.items():
    age = age + 10
    print(user, age)

