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

FN = "input/23.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

adj = defaultdict(set)
computers = set()
for line in s.split("\n"):
    a, b = line.split("-")
    adj[a].add(b)
    adj[b].add(a)
    computers.add(a)
    computers.add(b)

computers = list(computers)
n = len(computers)

ans1 = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = computers[i], computers[j], computers[k]
            if b in adj[a] and c in adj[a] and a in adj[b] and c in adj[b] and a in adj[c] and b in adj[c]:
                if a[0] == "t" or b[0] == "t" or c[0] == "t":
                    ans1 += 1
print(ans1)

vis = set()
def dfs(u):
    if u in vis:
        return
    vis.add(u)
    for v in adj[u]:
        for o in vis:
            if v not in adj[o]:
                break
        else:
            dfs(v)

best = set()
for s in computers:
    dfs(s)
    if len(vis) > len(best):
        best = vis.copy()
    vis.clear()

ans2 = ','.join(sorted(best))
print(ans2)