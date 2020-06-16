"""
You are given a date. Your task is to find what the day is on that date.


"""

import calendar
user_input = list(map(int, input().split()))
month = user_input[0]
day = user_input[1]
year = user_input[2]
c = calendar.weekday(year, month, day)
if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c == 3:
    print("THURSDAY")
elif c == 4:
    print("FRIDAY")
elif c == 5:
    print("SATURDAY")
else :
    print("SUNDAY")