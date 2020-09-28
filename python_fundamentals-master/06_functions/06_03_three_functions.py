'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

# zombie apocalypse - a zombie has been invited to a party.  How many people in town get infected?




def zombie_apocalypse(people_at_party):
    new_zombies = people_at_party * 5
    def zombie_apocalypse1(zombo1):
        new_zombies = zombo1 * 7
        def zombie_apocalypse2(zombo2):
            new_zombies = people_at_party * 12

            zombie_apocalypse2(people_at_party)
        zombie_apocalypse1(zombie_apocalypse2())
    zombie_apocalypse(zombie_apocalypse1())

party_goers = int(input("Enter the number of people at a party: "))
x = zombie_apocalypse(party_goers)
print(x)

