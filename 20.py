from collections import Counter, defaultdict, deque
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf
from operator import ior
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/20.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

g = [list(r) for r in s.split("\n")]
n, m = len(g), len(g[0])
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            g[i][j] = '.'
            start = i, j
        if g[i][j] == 'E':
            g[i][j] = '.'
            end = i, j

ok = lambda i, j: 0 <= i < n and 0 <= j < m and g[i][j] != '#'
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = [start]
vis = set()
dist = 0
pi, pj = -1, -1
i, j = start
g[i][j] = 0
while (i, j) != end:
    dist += 1
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ok(ni, nj) and (ni, nj) != (pi, pj):
            pi, pj = i, j
            i, j = ni, nj
            break
    g[i][j] = dist


def solve(cheat_range):
    ans = 0
    for i1 in range(1, n-1):
        for j1 in range(1, m-1):
            if g[i1][j1] == '#':
                continue
            for di in range(-cheat_range, cheat_range+1):
                for dj in range(-cheat_range, cheat_range+1):
                    man = abs(di) + abs(dj)
                    if not 2 <= man <= cheat_range:
                        continue
                    i2, j2 = i1+di, j1+dj
                    if not ok(i2, j2):
                        continue
                    diff = g[i2][j2] - g[i1][j1] - man
                    if diff >= 100:
                        ans += 1
    return ans


print(solve(2))
print(solve(20))