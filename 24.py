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

FN = "input/24.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

ch1, ch2 = s.split("\n\n")
mp = {}
for l in ch1.split("\n"):
    k, v = l.split(": ")
    v = int(v)
    mp[k] = v


lut = {
    "AND": iand,
    "XOR": xor,
    "OR": ior,
}

# t1 = A ^ B
# S = t1 ^ Cin
# q1 = A & B
# q2 = t1 & Cin
# Cout = q1 | q2

adj = defaultdict(set)
funcs = {}

# I did this by hand...
# python 24.py | dot -Tpng > out.png

# transform_mp = {
#     "kqk": "z15",
#     "cgq": "z23",
#     "fnr": "z39",
#     "svm": "nbc",
# }
# transform_mp |= {v: k for k, v in transform_mp.items()}
# def transform(s):
#     return transform_mp.get(s, s)

# print(",".join(sorted(transform_mp.keys())))
# exit()

for l in ch2.split("\n"):
    ks, v = l.split(" -> ")
    k1, op, k2 = ks.split(" ")
    # v = transform(v)
    funcs[v] = (k1, op, k2)
    adj[k2].add(v)
    adj[k1].add(v)

def topsort_(u, adj, vis, st):
    if u in vis:
        return
    vis.add(u)
    if u in adj:
        for v in adj[u]:
            topsort_(v, adj, vis, st)
    st.append(u)

def topsort(adj):
    st = []
    vis = set()
    for s in adj.keys():
        topsort_(s, adj, vis, st)
    return st[::-1]

print("digraph {")
for v in topsort(adj):
    if v not in mp:
        k1, op, k2 = funcs[v]
        print(f"  {k1}{op}{k2} [label={op}, shape=box]")
        print(f"  {k1} -> {k1}{op}{k2}")
        print(f"  {k2} -> {k1}{op}{k2}")
        print(f"  {k1}{op}{k2} -> {v}")
        mp[v] = lut[op](mp[k1], mp[k2])
print("}")

zs = sorted((kv for kv in mp.items() if kv[0][0] == "z"), reverse=True)
bits = ''.join(str(x[1]) for x in zs)
ans1 = int(bits, 2)
# print(ans1)
