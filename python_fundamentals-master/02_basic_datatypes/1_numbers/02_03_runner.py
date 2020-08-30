'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
distance_ran_miles = 10
time_taken_seconds = (30 * 60) + 30
time_taken_hours = (time_taken_seconds/60)/60
speed_in_miles = distance_ran_miles/time_taken_hours
print(speed_in_miles)
speed_in_kilometres = speed_in_miles * 1.6
print("The runners' speed in kilometres per hour is " + str(round(speed_in_kilometres, 2)))





