'''
Write a function named add_ten() that takes a dictionary whose values are numbers. The function should add 10 to every even value in the dictionary.
'''

def add_ten(d):
    for key, value in d.items():
        if value % 2 == 0:
            d[key] = value + 10

    return d


