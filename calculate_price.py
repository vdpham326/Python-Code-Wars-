'''
Given a pricelist in the template, write a function named calculate_price() that takes a dictionary structured in the following format:

customer_order = {
    'cheese': 3,
    'coke': 2
}
The customer order contains a list of item purchases with quantities as values. The function should return the total cost for the whole order. 
If a given item is not present in the pricelist, simply ignore it.
'''

pricelist = {'bread': 2.37, 'ham': 3.48, 'cheese': 3.09, 'water': 1.19, 'coke': 2.58, 'juice': 4.18, 'butter': 5.18}

customer_order = {
    'cheese': 3,
    'coke': 2
}

def calculate_price(di):
    sum_cost = 0

    for key in di:
        if key in pricelist:
            sum_cost += (di[key] * pricelist[key])
    return sum_cost

print(calculate_price(customer_order))
