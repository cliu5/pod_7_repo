import sys

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
name = input("Please enter your name: ")

# TODO: Write code to ask the client his savings and save it to another variable.
savings = input("Please enter amount in savings: ")
savings = int(savings)

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft: ")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.


if stock == "amzn":
    purchase = round(savings / amazon, 2)
    stockN = "Amazon"
    stockP = amazon

elif stock == "aapl":
    purchase = round(savings / apple, 2)
    stockN = "Apple"
    stockP = apple

elif stock == "fb":
    purchase = round(savings / fb, 2)
    stockN = "Facebook"
    stockP = fb

elif stock == "goog":
    purchase = round(savings / google, 2)
    stockN = "Google"
    stockP = google

elif stock == "msft":
    purchase = round(savings / msft, 2)
    stockN = "Microsoft"
    stockP = msft

else: sys.exit("Incorrect stock ticker entered, try again")
   
print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{name} has ${savings} in savings and can buy {purchase} shares of {stockN} at the current price of ${stockP}")

print()

