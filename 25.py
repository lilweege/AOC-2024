from collections import Counter, defaultdict, deque
from itertools import pairwise, product
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf
from operator import ior, iand, xor
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/25.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

chunks = s.split("\n\n")
keys = []
locks = []
for chunk in chunks:
    lines = chunk.split("\n")
    n, m = len(lines), len(lines[0])
    isLock = lines[0].count("#") == len(lines[0])
    pat = []
    for j in range(m):
        cnt = 0
        for i in range(n):
            cnt += lines[i][j] == '#'
        pat.append(cnt-1)
    pat = tuple(pat)
    if isLock:
        locks.append(pat)
    else:
        keys.append(pat)

ans = 0
for key in keys:
    for lock in locks:
        if all(x+y <= m for x, y in zip(key, lock)):
            ans += 1
print(ans)