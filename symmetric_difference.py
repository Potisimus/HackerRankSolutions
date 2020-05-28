"""
Given 2 sets of integers, M and N, print their symmetric difference
in ascending order. The term symmetric difference
indicates those values that exist in either  M or N  but do not exist in both.
"""
m = input()
set_m = set(map(int, input().split()))
n = input()
set_n = set(map(int, input().split()))


print(*sorted(set_m ^ set_n, key=int), sep='\n')
