'''
Write a function named max_value() that takes a dictionary and returns its greatest value. Assume that all values in the dictionary are natural numbers.
'''

def max_value(d):
    largest = 0
    for value in d.values():
        if value > largest:
            largest = value
    return largest

