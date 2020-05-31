"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps.
She decided to count the total number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from
a stack of  country stamps.

Find the total number of distinct country stamps.
"""

country_no = int(input())
s = set()
for i in range(country_no):
    country_name = input()
    s.add(country_name)

print(len(s))
