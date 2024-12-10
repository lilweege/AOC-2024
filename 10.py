from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import partial
import re

FN = "input/10.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
g = [list(r) for r in s.split("\n")]
n, m = len(g), len(g[0])

trailheads = []
for i in range(n):
    for j in range(m):
        if g[i][j] == '0':
            trailheads.append((i, j))
ok = lambda i, j: 0 <= i < n and 0 <= j < m
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start):
    vis = set()
    q = [start]
    nines = set()
    while q:
        b, q = q, []
        for (i, j) in b:
            if g[i][j] == '9':
                nines.add((i, j))
                continue
            if (i, j) in vis:
                continue
            vis.add((i, j))
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ok(ni, nj):
                    if int(g[ni][nj]) == int(g[i][j]) + 1:
                        q.append((ni, nj))
    return len(nines)

def dfs(i, j):
    if g[i][j] == '9':
        return 1
    cnt = 0
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if ok(ni, nj):
            if int(g[ni][nj]) == int(g[i][j]) + 1:
                cnt += dfs(ni, nj)
    return cnt

ans1 = sum(bfs(start) for start in trailheads)
ans2 = sum(dfs(*start) for start in trailheads)

print(ans1)
print(ans2)