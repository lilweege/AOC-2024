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

FN = "input/21.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
numpad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}
numpad_rev = {v: k for k, v in numpad.items()}
numpad_ok = lambda i, j: 0 <= i < 4 and 0 <= j < 3 and not (i == 3 and j == 0)


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
keypad = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}
keypad_ok = lambda i, j: 0 <= i < 2 and 0 <= j < 3 and not (i == 0 and j == 0)
keypad_step = {
    (0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'
}

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

@cache
def numpad_sequences(s, t):
    start, target = numpad[s], numpad[t]
    q = [[start, []]]
    ans = []
    while q:
        b, q = q, []
        for (i, j), steps in b:
            if (i, j) == target:
                ans.append(''.join(keypad_step[x] for x in steps))
                continue
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if numpad_ok(ni, nj):
                    q.append(((ni, nj), steps+[(di, dj)]))
        if ans:
            break
    return ans


@cache
def keypad_cost(s, t, dep):
    if dep == 0:
        return 1
    if s == t:
        return 1
    start, target = keypad[s], keypad[t]
    q = [((start,), "")]
    ans = inf
    while q:
        b, q = q, []
        for path, steps in b:
            i, j = path[-1]
            if (i, j) == target:
                total = sum(keypad_cost(fr, to, dep-1) for fr, to in pairwise('A'+steps+'A'))
                ans = min(ans, total)
                continue
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if keypad_ok(ni, nj) and (ni, nj) not in path:
                    q.append((path+((ni, nj),), steps+keypad_step[(di, dj)]))
    return ans

def solve(code, num_kps):
    num = int(code[:-1])
    ans = inf
    num_seqs = [numpad_sequences(u, v) for u, v in pairwise('A'+code)]
    for seq in product(*num_seqs):
        seq = 'A'+'A'.join(seq)+'A'
        ans = min(ans, sum(keypad_cost(a, b, num_kps) for a, b in pairwise(seq)))
    return ans * num


ans1 = sum(solve(code, 2) for code in s.split("\n"))
print(ans1)
ans2 = sum(solve(code, 25) for code in s.split("\n"))
print(ans2)