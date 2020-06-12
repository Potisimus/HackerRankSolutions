"""
Task:
You are given a two lists A and B. Your task is to compute their cartesian product A X B.


"""
from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))
itr_product = list(product(A,B))
for i in range(len(itr_product)):
    print(itr_product[i], end= " ")(A,B)