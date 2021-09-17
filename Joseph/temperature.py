'''
### The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

1. Convert a temperature of 100 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_100`, and use `print()` to print out the value
    * Is the resulting temperature you get an integer or float? How do you know?
2. Convert a temperature of 0 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_0`, and use `print()` to print out the value
3. Convert a temperature of 34.2 degrees fahrenheit to celsius
    * Do this one all in one print statement **without** saving any variables
'''
# 1.
# formula to convert 100 degrees fahrenheit to celsius
celsius_100 = (100-32)*(5/9)
print(celsius_100)  # results of formula
print(type(celsius_100))  # checking type of results

# 2.
celsius_0 = (0-32)*(5/9)  # formula to convert 0 degrees fahrenheit to celsius
print(celsius_0)  # results of formula
print(type(celsius_0))  # checking type of results

# 3. Converting the temperature of 34.2 fahrenheit to celsius in a single statement
print((34.2)*(5/9))

'''
4. Convert a temperature of 5 degrees celsius to fahrenheit?
5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
'''

# 4. Converting the temperature of 5 degrees celsius to fahrenheit
print((5*(9/5))+32)

# 5. Converting the temperature of 30.2 degrees celsius to fahrenheit
print((32.2*(9/5))+32)
# 30.2 degrees celsius is greater than 85.1 degrees fahrenheit
