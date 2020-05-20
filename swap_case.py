"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters
and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

"""
import string


def swap_case(s):
    new_string = ""
    for i in range(len(s)):
        if s[i].isspace():
            new_string += " "
        elif s[i].isdigit():
            new_string += s[i]
        elif s[i] in string.punctuation:
            new_string += s[i]
        elif s[i].isupper():
            new_string += s[i].lower()
        elif s[i].islower():
            new_string += s[i].upper()
    print(new_string)


swap_case("Www.HackerRank.com")
