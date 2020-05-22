"""
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Design

 Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""

number1, number2 = map(int, input().split())
horizontal_pattern = "-"
vertical_pattern = ".|."
multiple = number2 // number1
numbers_of_horizontal = (number1 // 2) * multiple
numbers_of_vertical = 1

for i in range(number1 // 2):
    print(
        horizontal_pattern * numbers_of_horizontal + vertical_pattern * numbers_of_vertical + horizontal_pattern * numbers_of_horizontal)
    numbers_of_horizontal = (numbers_of_horizontal - multiple)
    numbers_of_vertical = (numbers_of_vertical + (multiple - 1))

print(horizontal_pattern * ((number2 - 7) // 2) + "WELCOME" + horizontal_pattern * ((number2 - 7) // 2))
numbers_of_horizontal = numbers_of_horizontal + multiple
numbers_of_vertical = numbers_of_vertical - 2
for i in range(number1 // 2):
    print(
        horizontal_pattern * numbers_of_horizontal + vertical_pattern * numbers_of_vertical + horizontal_pattern * numbers_of_horizontal)
    numbers_of_horizontal = (numbers_of_horizontal + multiple)
    numbers_of_vertical = (numbers_of_vertical - (multiple - 1))
