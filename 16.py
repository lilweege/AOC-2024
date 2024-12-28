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

FN = "input/16.txt"
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

def part1():
    d = 0
    pq = [(0, start[0], start[1], d)]
    dist = [[[inf] * 4 for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]][d] = 0

    while pq:
        c, i, j, d = heappop(pq)

        if (i, j) == end:
            return c

        for nd, (di, dj) in enumerate(dirs):
            ni, nj = i + di, j + dj

            if ok(ni, nj):
                nc = c + 1
                if d != nd: nc += 1000
                if nc < dist[ni][nj][nd]:
                    dist[ni][nj][nd] = nc
                    heappush(pq, (nc, ni, nj, nd))
    assert 0


def part2():
    d = 0
    pq = [(0, start[0], start[1], d, [start])]
    dist = [[[inf] * 4 for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]][d] = 0

    paths = []
    best_c = inf
    while pq:
        c, i, j, d, p = heappop(pq)

        if (i, j) == end:
            if c < best_c:
                best_c = c
                paths = [p]
            elif c == best_c:
                paths.append(p)
            continue

        for nd, (di, dj) in enumerate(dirs):
            ni, nj = i + di, j + dj

            if ok(ni, nj):
                nc = c + 1
                if d != nd: nc += 1000
                if nc <= dist[ni][nj][nd]:
                    dist[ni][nj][nd] = nc
                    heappush(pq, (nc, ni, nj, nd, p + [(ni, nj)]))

    ans = len(reduce(ior, map(set, paths)))
    return ans

print(part1())
print(part2())