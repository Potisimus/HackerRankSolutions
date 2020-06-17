"""
Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

"""

from collections import OrderedDict
ordered_dictionary = OrderedDict()
num = int(input())
for i in range (num):
    item, space, price = input().rpartition(' ')
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)
for item, price in ordered_dictionary.items():
    print(item, price)
