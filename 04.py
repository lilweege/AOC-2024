from collections import Counter
from itertools import pairwise
import re

FN = "input/04.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

g = s.split("\n")
m, n = len(g), len(g[0])
get = lambda i, j: g[i][j] if 0 <= i < n and 0 <= j < m else "?"

ans1 = 0
for i in range(n):
    for j in range(m):
        if get(i, j) + get(i, j+1) + get(i, j+2) + get(i, j+3) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i, j-1) + get(i, j-2) + get(i, j-3) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i+1, j) + get(i+2, j) + get(i+3, j) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i-1, j) + get(i-2, j) + get(i-3, j) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i-1, j-1) + get(i-2, j-2) + get(i-3, j-3) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i+1, j+1) + get(i+2, j+2) + get(i+3, j+3) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i+1, j-1) + get(i+2, j-2) + get(i+3, j-3) == "XMAS":
            ans1 += 1
        if get(i, j) + get(i-1, j+1) + get(i-2, j+2) + get(i-3, j+3) == "XMAS":
            ans1 += 1
print(ans1)

ans2 = 0
for i in range(n):
    for j in range(m):
        s1 = get(i-1, j-1) + get(i, j) + get(i+1, j+1)
        s2 = get(i+1, j-1) + get(i, j) + get(i-1, j+1)
        if s1 in ("MAS", "SAM") and s2 in ("MAS", "SAM"):
            ans2 += 1
print(ans2)
