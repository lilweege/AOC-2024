from collections import Counter, defaultdict, deque
from itertools import pairwise, product
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf
from operator import ior
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/22.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
nums = list(map(int, s.split("\n")))
n = len(nums)
ans1 = 0
prices = []
for x in nums:
    prices.append([x%10])
    for _ in range(2000):
        x = (x * 64) ^ x
        x %= 16777216
        x = (x // 32) ^ x
        x %= 16777216
        x = (x * 2048) ^ x
        x %= 16777216
        a = x % 10
        prices[-1].append(a)
    ans1 += x
print(ans1)

diffs = [[y-x for x, y in pairwise(l)] for l in prices]
assert len(diffs) == n
m = len(diffs[0])
assert m == 2000

mp = defaultdict(lambda: defaultdict(list))
for j in range(m-4):
    for i in range(n):
        w = tuple(diffs[i][j:j+4])
        # windows.add(w)
        if i not in mp[w]:
            mp[w][i] = prices[i][j+4]

ans2 = max(sum(x.values()) for x in mp.values())
print(ans2)