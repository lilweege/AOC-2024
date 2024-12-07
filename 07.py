from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import partial
import re

FN = "input/07.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()


def concat(a, b):
    return a * (10 ** len(str(b))) + b


def solve(y, xs, part2):
    n = len(xs)

    def dfs(x, i):
        if i == n:
            return x == y
        if dfs(x * xs[i], i + 1):
            return True
        if dfs(x + xs[i], i + 1):
            return True
        if part2 and dfs(concat(x, xs[i]), i + 1):
            return True
        return False

    return dfs(xs[0], 1)

part1 = partial(solve, part2=False)
part2 = partial(solve, part2=True)

ans1 = ans2 = 0
for l in s.split("\n"):
    y, xs = l.split(": ")
    y = int(y)
    xs = list(map(int, xs.split()))

    if part1(y, xs): ans1 += y
    if part2(y, xs): ans2 += y

print(ans1)
print(ans2)