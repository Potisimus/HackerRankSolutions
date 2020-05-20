"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs
in the given string. String traversal will take place from left to right,
not from right to left.

Sample Input

ABCDCDC
CDC

Sample Output

2

"""


def count_substring(string, sub_string):
    count =0
    indx = None
    for i in range(len(string)):
        if len(sub_string) < len(string):
            indx = string.find(sub_string)
            if indx >=0:
                count+=1
            string=string[(indx+1): ]
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
