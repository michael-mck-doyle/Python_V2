'''
Trip Cost Calculator
Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

Specs
Receive the following arguments from the user:

kilometers to drive
liters-per-kilometer usage of the car
price per liter of fuel
Calculate the cost of the trip and display it to the user in the console.
'''

distance = input("Please enter the kilometer distance of the trip: ")
litres_per_km = input("Enter the number of kilometers you can travel with one litre of fuel: ")
price_per_litre = input("Enter the cost of a litre of fuel: ")
cost_of_trip = (int(distance) / int(litres_per_km)) * int(price_per_litre)

print("The total cost of the trip is: " + str(cost_of_trip))
