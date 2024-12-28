from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial
import re

import sys
sys.setrecursionlimit(9999)

FN = "input/12.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

g = [list(r) for r in s.split("\n")]
n, m = len(g), len(g[0])

ok = lambda i, j: 0 <= i < n and 0 <= j < m
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

vis = set()
nodes = set()
def dfs(i, j):
    if (i, j) in vis:
        return 0
    nodes.add((i, j))
    vis.add((i, j))
    area = 1
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if ok(ni, nj) and g[ni][nj] == g[i][j]:
            area += dfs(ni, nj)
    return area

def part1():
    ans = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in vis:
                nodes.clear()
                area = dfs(i, j)
                perimeter = 0
                for ii, jj in nodes:
                    col = g[ii][jj]
                    for di, dj in dirs:
                        ni, nj = ii+di, jj+dj
                        if not ok(ni, nj) or g[ni][nj] != col:
                            perimeter += 1
                ans += area * perimeter
    return ans

def part2():
    class UnionFind:
        def __init__(self, n):
            self.par = list(range(n))
            self.sz = [1] * n

        def find(self, x):
            if self.par[x] != x:
                self.par[x] = self.find(self.par[x])
            return self.par[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x != y:
                if self.sz[x] < self.sz[y]:
                    self.par[x] = y
                    self.sz[y] += self.sz[x]
                else:
                    self.par[y] = x
                    self.sz[x] += self.sz[y]

        def connected(self, x, y):
            return self.find(x) == self.find(y)

        def size(self, x):
            x = self.find(x)
            return self.sz[x]


    global n, m, g

    scl = 5
    dbl_g = [[' '] * (scl*m) for _ in range(scl*n)]
    for i in range(n):
        for j in range(m):
            for di in range(scl):
                for dj in range(scl):
                    dbl_g[i*scl+di][j*scl+dj] = g[i][j]
    g = dbl_g
    n *= scl
    m *= scl
    def index(i, j):
        return i*m + j

    ans = 0
    vis.clear()
    for i in range(n):
        for j in range(m):
            if (i, j) not in vis:
                nodes.clear()
                area = dfs(i, j)
                perimNeighbors = defaultdict(int)
                for ii, jj in nodes:
                    col = g[ii][jj]
                    for di, dj in dirs:
                        ni, nj = ii+di, jj+dj
                        if not ok(ni, nj) or g[ni][nj] != col:
                            perimNeighbors[(ii, jj)] += 1

                uf = UnionFind(n*m)
                for ii, jj in perimNeighbors:
                    for normIdx, (di, dj) in enumerate(dirs):
                        ni, nj = ii + di, jj + dj
                        if not ok(ni, nj) or g[ni][nj] != g[ii][jj]:
                            adjIdx1 = (normIdx+1) % 4
                            adjIdx2 = (normIdx+3) % 4
                            di1, dj1 = dirs[adjIdx1]
                            di2, dj2 = dirs[adjIdx2]
                            ni1, nj1 = ii + di1, jj + dj1
                            ni2, nj2 = ii + di2, jj + dj2
                            if (ni1, nj1) in perimNeighbors and perimNeighbors[(ni1, nj1)] == 1 and (ni2, nj2) in perimNeighbors and perimNeighbors[(ni2, nj2)] == 1:
                                uf.union(index(ii, jj), index(ni1, nj1))
                                uf.union(index(ii, jj), index(ni2, nj2))
                            break
                wallSet = set()
                for ii, jj in perimNeighbors:
                    if uf.size(index(ii, jj)) >= 2:
                        root = uf.find(index(ii, jj))
                        wallSet.add(root)
                walls = len(wallSet)
                ans += area//(scl**2) * (walls)

    return ans

print(part1())
print(part2())