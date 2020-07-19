'''
Write a function named get_congratulations(completed_info) that accepts a tuple with two values: the name of the student, and the datetime when the student finished the course. 
Your task is to return the following string:

{name}, congratulations! You've completed the course on {datetime}
The {datetime} should be formatted the following way:

Friday, 05 October 2018 at 01:30 PM
'''
import datetime

def get_congratulations(completed_info):
  name, date = completed_info
  date_new = date.strftime('%A, %d %B %Y at %I:%M %p')
  return f"{name}, congratulations! You've completed the course on {date_new}"

