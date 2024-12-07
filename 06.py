from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
import re

FN = "input/06.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
default_g = [list(r) for r in s.split("\n")]
n, m = len(default_g), len(default_g[0])
for i in range(n):
    for j in range(m):
        if default_g[i][j] == '^':
            default_g[i][j] = 'X'
            start = i, j

ok = lambda i, j: 0 <= i < n and 0 <= j < m
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def simulate():
    pos = start
    vis = set()
    d = 3
    while True:
        if (pos, d) in vis:
            return True
        vis.add((pos, d))
        di, dj = dirs[d]
        ni, nj = pos[0] + di, pos[1] + dj
        if not ok(ni, nj):
            break
        if g[ni][nj] == '#':
            d = (d + 1) % 4
            ni, nj = pos
        g[ni][nj] = 'X'
        pos = ni, nj
    return False

g = deepcopy(default_g)
simulate()
ans1 = sum(row.count('X') for row in g)
print(ans1)

# LOL
ans2 = 0
for i in range(n):
    for j in range(m):
        g = [row.copy() for row in default_g]
        if g[i][j] == '.':
            g[i][j] = '#'
            if simulate():
                ans2 += 1
print(ans2)
