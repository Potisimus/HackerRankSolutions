"""
You are given a set A and N number of other sets.
These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
"""

_ = int(input())
s1 = set(map(int,input().split()))
N = int(input())

for _ in range(N):
    cmd, _ = input().split()
    s2 = set(map(int, input().split()))
    if (cmd == "intersection_update"):
        s1.intersection_update(s2)
    elif (cmd == "update"):
        s1.update(s2)
    elif (cmd == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif (cmd == "difference_update"):
        s1.difference_update(s2)
print(sum(s1))
