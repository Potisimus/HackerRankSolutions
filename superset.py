"""
Check if a set is strict super set of two other sets
if it is super set for both of them print True
otherwise print False
"""

set_a = set(map(int, input().split()))
new_set_number = int(input())
set_b = set(map(int, input().split()))
set_c = set(map(int, input().split()))
if set_a.issuperset(set_b) and set_a.issuperset(set_c):
    print(True)
else:
    print(False)