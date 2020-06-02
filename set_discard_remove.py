"""
Task
You have a non-empty set , and you have to execute N commands given in  N lines.

The commands will be pop, remove and discard.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

Sample Output

4

"""
n = int(input())
s = set(map(int, input().split()))

methods = {
    'pop': s.pop,
    'remove': s.remove,
    'discard': s.discard

}

args = None

for _ in range(int(input())):
    method, *args = input().split()

    if len(args) > 1:
        [methods[method](*map(int, arg)) for arg in args]
    else:
        methods[method](*map(int,args))

print(sum(s))
