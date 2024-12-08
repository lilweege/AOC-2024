from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import partial
import re

FN = "input/08.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

g = [list(r) for r in s.split("\n")]
N, M = len(g), len(g[0])
ok = lambda i, j: 0 <= i < N and 0 <= j < M

nodes = defaultdict(list)
for i in range(N):
    for j in range(M):
        if g[i][j] != '.':
            nodes[g[i][j]].append((i, j))

def solve(one_step):
    for l in nodes.values():
        n = len(l)
        for i in range(n):
            for j in range(i+1, n):
                (ai, aj), (bi, bj) = l[i], l[j]
                di = bi-ai
                dj = bj-aj

                ni = ai-di
                nj = aj-dj
                while ok(ni, nj):
                    g[ni][nj] = '#'
                    ni -= di
                    nj -= dj
                    if one_step:
                        break

                ni = bi+di
                nj = bj+dj
                while ok(ni, nj):
                    g[ni][nj] = '#'
                    ni += di
                    nj += dj
                    if one_step:
                        break

solve(one_step=True)
ans1 = sum(sum(x == '#' for x in r) for r in g)
print(ans1)

solve(one_step=False)
ans2 = sum(sum(x != '.' for x in r) for r in g)
print(ans2)