'''
Write a function named calculate_discount() that takes two dictionaries: base_prices and discounts. Both dictionaries have strings as keys and integers as values. 
For each item in base_prices, if there is an item with the same key in discounts, subtract the discounts value from the base_prices value. Return a dictionary with the new, discounted prices. 
If there was no discount for a given item, return it as it was
'''
def calculate_discount(base_prices, discounts):
    discounted_prices = base_prices.copy() # empty dictionary

    for key, value in base_prices.items():
        for key2, value2 in discounts.items():
            if  key == key2:
                discounted_prices[key] = value - value2
    return discounted_prices