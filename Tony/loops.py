print('Lets get loopy!')

# For loops
# For each item in a group of items:
#   do something with that item

laundry_basket = ['jeans', 'sweater', 'tank top', 'dress shirt']

# for each garment in our laundry basket:
#   fold the garment
#   put away the garment

for garments in laundry_basket:
       print('Fold the ', garments.upper())
       print('Put away the ', garments.upper())
       print()
print('Eat your chocolate!')


# For loops with the range function
# For each number in a range of number:
#   do something with that number

print(list(range(len(laundry_basket))))

laundry_basket = ['jeans', 'sweater', 'tank top', 'dress shirt']

for index in range(len(laundry_basket)):
    print(f'The garment at index {index} is {laundry_basket[index]}')
print()


correct_password = 'password_123'

# While Loops
# while a condition is true:w
#   keep going

password = ''
while password != correct_password:
    password = input("Please enter your password: ")
