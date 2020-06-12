"""
You are given a string S.
Your task is to print all possible permutations of
size K of the string in lexicographic sorted order.
"""
from itertools import permutations
str, n = input().split()
n = int(n)
itr_permutation = sorted(list(permutations(str,n)))

for i in range (len(itr_permutation)):
    print(''.join(itr_permutation[i]))