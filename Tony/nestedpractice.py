#dictionary inside a dictionary
#lists inside a dictionary
#dictionaries in a list
#lists in a list
#dictionary inside a list inside a dictionary

#How to get AND update information within nested data structures

cart = {
        'cleaning_products': ['soap', 'broom']
}

cart['cleaning_products'].append('mop')
cart['cleaning_products'].append('lysol')

#adding a new list as a value in the dictionary
cart['tooth_care'] = ['toothbrush', 'floss', 'mouthwash']

#removing from list is done through remove, pop is used for dictionary
cart['tooth_care'].remove('floss')

cart.pop('cleaning_products')

print(cart['tooth_care'])

cart['home_improvement'] = {'shovel' : 27.99,
                            'duct_tape' : 2.17,
                            'paint' : 17.43}

print(cart)

print(cart['home_improvement']['shovel'])

#lists are ORDERED so we use indexes, dictionaries use keys and are UNORDERED








