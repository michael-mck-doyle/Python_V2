'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_amount = (int(input("Please enter the amount you want to invest: ")))
interest_rate = (int(input("Please enter the interest rate you want to invest at (in percentage): ")))
years_of_investment = (int(input("Please enter the number of years you want to invest for: ")))

future_value = investment_amount * (1 + interest_rate/100)**years_of_investment

print("The value of your investment after " + str(years_of_investment) + " is = " + str(round(future_value, 2)))

