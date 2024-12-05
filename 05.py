from collections import Counter, defaultdict
from itertools import pairwise
import re

FN = "input/05.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
a, b = s.split("\n\n")
adj = defaultdict(set)
for l in a.split("\n"):
    u, v = map(int, l.split("|"))
    adj[u].add(v)

ans1 = ans2 = 0
for l in b.split("\n"):
    order = list(map(int, l.split(",")))
    n = len(order)
    ok = True
    for i in range(n):
        for j in range(i):
            u, v = order[j], order[i]
            if u in adj[v]: ok = False
        for j in range(i+1, n):
            u, v = order[i], order[j]
            if u in adj[v]: ok = False

    if ok:
        ans1 += order[n//2]
    else:
        new_order = []
        for v in order:
            for i, u in enumerate(new_order):
                if u in adj[v]:
                    new_order.insert(i, v)
                    break
            else:
                new_order.append(v)
        ans2 += new_order[n//2]

print(ans1)
print(ans2)