# declare variables
celsius_100 = 100

celsius_0 = 0
# conversion functions
def fahrenheight_to_celsius(temp):
    return (temp - 32) * (5/9)

def celsius_to_fahrenheight(temp):
    return (temp * 9/5 + 32)
# Step 1
print(fahrenheight_to_celsius(celsius_100))
# Step 2
print(fahrenheight_to_celsius(celsius_0))
#Step 3
print((34.2 -32) * (5/9))
# Backwards
print(celsius_to_fahrenheight(5))
# check if 30.2 celsius is greater than 85.1 degrees fahrenheight
if 30.2 > fahrenheight_to_celsius(85.1):
    print('30.2 degrees celsius is greater')
else:
    print('85.1 degrees celsius is greater')
