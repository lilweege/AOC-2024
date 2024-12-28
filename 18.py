from collections import Counter, defaultdict, deque
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf
from operator import ior
import re

def pg(g):
    for r in g:print(''.join(r))

# import sys
# sys.setrecursionlimit(9999)

FN = "input/18.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

coords = [tuple(map(int, l.split(","))) for l in s.split("\n")]
# N = 6
N = 70


def solve(max_coords):
    ok = lambda i, j: 0 <= i <= N and 0 <= j <= N and g[i][j] != '#'
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    g = [['.']*(N+1) for _ in range(N+1)]
    for x, y in coords[:max_coords]:
        g[y][x] = '#'
    q = [(0, 0)]
    vis = set()
    dep = 0
    while q:
        b, q = q, []
        for i, j in b:
            if (i, j) in vis:
                continue
            vis.add((i, j))
            if (i, j) == (N, N):
                return dep
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ok(ni, nj) and (ni, nj) not in vis:
                    q.append((ni, nj))
        dep += 1
    return -1


def part1():
    return solve(1024)


def part2():
    # for best in reversed(range(len(coords))):
    #     if solve(best) != -1:
    #         break
    lo, hi = 1024, len(coords)
    best = 1024
    while lo < hi:
        mi = (lo + hi) // 2
        ans = solve(mi)
        if ans == -1:
            hi = mi
        else:
            lo = mi + 1
            best = mi
    bx, by = coords[best]
    return f"{bx},{by}"


print(part1())
print(part2())
