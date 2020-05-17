'''
Given an integer, n, and n space-separated integers as input,
create a tuple , t, of those  integers. Then compute and
print the result of hash(t).

Input:
2
1 2

Output:
3713081631934410656


'''

import  hashlib
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print (hash(integer_list))
