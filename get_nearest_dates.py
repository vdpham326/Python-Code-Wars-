'''
Write a function named get_nearest_dates() that returns a tuple with three dates: yesterday, today, and tomorrow (respectively).
'''

import datetime

def get_nearest_dates():
  today = datetime.date.today()
  yesterday = today - datetime.timedelta(days=1)
  tomorrow = today + datetime.timedelta(days=1)
  return (yesterday, today, tomorrow)