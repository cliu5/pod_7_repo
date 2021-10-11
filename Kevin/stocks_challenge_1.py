print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input('What is your name? ')
# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input('How much money is in your savings? '))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog'\
     for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to\
#  find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn':
    number_of_stocks = savings / amazon
    if number_of_stocks > 1:
        print(f'{name} has ${savings} and can purchase {number_of_stocks} of Amazon at the price of ${amazon}')
    else:
        print('You don\'t have enough money to buy Amazon stock')
elif stock == 'aapl':
    number_of_stocks = savings / apple
    if number_of_stocks > 1:
        print(f'{name} has ${savings} and can purchase {number_of_stocks} of Apple at the price of ${apple}')
    else:
        print('You don\'t have enough money to buy Apple stock')
elif stock == 'fb':
    number_of_stocks = savings / fb
    if number_of_stocks > 0:
        print(f'{name} has ${savings} and can purchase {number_of_stocks} of Facebook at the price of ${fb}')
    else:
        print('You don\'t have enough money to buy Facebook stock')
elif stock == 'goog':
    number_of_stocks = savings / google
    if number_of_stocks > 0:
        print(f'{name} has ${savings} and can purchase {number_of_stocks} of Google at the price of ${google}')
    else:
        print('You don\'t have enough money to buy Google stock')
elif stock == 'msft':
    number_of_stocks = savings / msft
    if number_of_stocks > 0:
        print(f'{name} has ${savings} and can purchase {number_of_stocks} of Microsoft at the price of ${msft}')
    else:
        print('You don\'t have enough money to buy Microsoft stock')
else:
    print('You did not enter a valid stock')

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

# print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()

