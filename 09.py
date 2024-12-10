from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import partial
import re

FN = "input/09.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

def part1():
    n = len(s)
    isBlk = True
    x = 0
    seq = []
    for c in s:
        c = int(c)
        if isBlk:
            seq.extend([x] * c)
            x += 1
        else:
            seq.extend(["."]  * c)
        isBlk = not isBlk

    n = len(seq)
    ans = 0

    i = 0
    j = n-1
    idx = 0
    while i <= j:
        if seq[i] != ".":
            ans += idx * seq[i]
            i += 1
        elif seq[i] == '.':
            i += 1
            while i <= j and seq[j] == ".":
                j -= 1
            if i > j: break
            ans += idx * seq[j]
            j -= 1
        idx += 1
    return ans

def part2():
    n = len(s)
    isBlk = True
    x = 0
    seq = []
    for c in s:
        c = int(c)
        if isBlk:
            seq.append([x, c, c])
            x += 1
        else:
            seq.append([".", c, c])
        isBlk = not isBlk

    ans = 0
    n = len(seq)
    for j in reversed(range(n)):
        c, cnt, oldcnt = seq[j]
        if c != '.':
            idx = 0
            for i in range(j):
                c2, space, oldspace = seq[i]
                if c2 == '.':
                    if space >= cnt:
                        idx += oldspace - space
                        seq[i][1] -= cnt
                        seq[j][0] = '?'
                        for _ in range(cnt):
                            ans += idx * c
                            idx += 1
                        break
                idx += oldspace

    idx = 0
    for i in range(n):
        c, cnt, oldcnt = seq[i]
        if c == '?' or c == '.':
            idx += oldcnt
            continue
        for _ in range(cnt):
            ans += idx * c
            idx += 1
    return ans

print(part1())
print(part2())