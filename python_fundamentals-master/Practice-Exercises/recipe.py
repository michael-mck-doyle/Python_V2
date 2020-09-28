# prepare a recipe using different ingredient classes and objects

class Ingredient:
    def __init__(self, name):
        self.name = name


i = Ingredient('spinach')
print(i.name)

j = Ingredient('corn')
print(j.name)


print(type(i))
