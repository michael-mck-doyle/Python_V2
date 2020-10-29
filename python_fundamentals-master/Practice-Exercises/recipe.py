# prepare a recipe using different ingredient classes and objects

class Ingredient:
    def __init__(self, name, colour, origin, amount):
        self.name = name
        self.colour = colour
        self.origin = origin
        self.amount = amount


i = Ingredient('spinach', 'green', 'South America', 3)
print(i.name, i.colour, i.origin, i.amount)

j = Ingredient('corn', 'yellow', 'kansas', 4)
print(j.name, j.colour, j.origin, j.amount)


print(type(i))
