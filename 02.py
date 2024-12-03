from collections import Counter
from itertools import pairwise

FN = "input/02.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

def is_safe(lst):
    if lst[0] < lst[1]:
        inc = True
    elif lst[0] > lst[1]:
        inc = False
    else:
        return False
    return all(1 <= (b-a if inc else a-b) <= 3 for a, b in pairwise(lst))

ans1 = 0
for l in s.split("\n"):
    lst = list(map(int, l.split()))
    if is_safe(lst):
        ans1 += 1
print(ans1)


ans2 = 0
for l in s.split("\n"):
    lst = list(map(int, l.split()))
    if is_safe(lst):
        ans2 += 1
    else:
        n = len(lst)
        for i in range(n):
            nlst = lst.copy()
            nlst.pop(i)
            if is_safe(nlst):
                ans2 += 1
                break

print(ans2)