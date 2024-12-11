from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial
import re

FN = "input/11.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

stones = list(map(int, s.split()))

cur = stones
nxt = []
for idx in range(25):
    for x in cur:
        s = str(x)
        n = len(s)
        if x == 0:
            nxt.append(1)
        elif n & 1:
            nxt.append(x * 2024)
        else:
            nxt.append(int(s[:n//2]))
            nxt.append(int(s[n//2:]))
    cur, nxt = nxt, []
ans1 = len(cur)
print(ans1)


@cache
def dfs(x, dep):
    if dep == 0:
        return 1
    if x == 0:
        return dfs(1, dep-1)
    s = str(x)
    n = len(s)
    if n & 1:
        return dfs(x * 2024, dep-1)
    return dfs(int(s[:n//2]), dep-1) + dfs(int(s[n//2:]), dep-1)

ans2 = sum(dfs(x, 75) for x in stones)
print(ans2)
