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

FN = "input/19.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

ch1, ch2 = s.split("\n\n")
dictionary = ch1.split(", ")
words = ch2.split("\n")

def countWordBreaks(s, words):
    N = len(s)
    dp = [0] * N
    for i in range(N):
        for word in words:
            n = len(word)
            if i < n-1:
                continue
            if i == n-1 or dp[i - n] > 0:
                if s[i-n+1:i+1] == word:
                    dp[i] += 1 if i == n-1 else dp[i-n]
    return dp[-1]

cnt = [countWordBreaks(word, dictionary) for word in words]

ans1 = sum(map(bool, cnt))
print(ans1)

ans2 = sum(cnt)
print(ans2)
