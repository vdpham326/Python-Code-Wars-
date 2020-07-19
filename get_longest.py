'''
Write a function named get_longest(*args) that accepts any number of string arguments and returns the longest string. 
If there are no arguments, return an empty string. If there is more than one string argument with the greatest length, return the first one.
'''

import datetime

def get_longest(*args):
  longest = 0
  longest_str = ''
  if len(args) == 0:
    return ""
  for arg in args:
    if len(arg) > longest:
      longest = len(arg)
      longest_str = arg
  return longest_str