'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

import math
import statistics
example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(nums):
    print("Max number: " + str(max(nums)))
    print("Min number: " + str(min(nums)))
    print("Average number: " + str(statistics.mean(nums)))
    print("Sum of numbers: " + str(sum(nums)))


stats(example_list)

# call the function below here
