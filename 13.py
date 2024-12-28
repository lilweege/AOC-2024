from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/13.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

def solve(part2):
    ans = 0
    for chunk in s.split("\n\n"):
        a, b, x = chunk.split("\n")
        a1, a2 = [int(aa[1:]) for aa in a.split(": ")[1].split(", ")]
        b1, b2 = [int(bb[1:]) for bb in b.split(": ")[1].split(", ")]
        X, Y = [int(xx[2:]) for xx in x.split(": ")[1].split(", ")]
        if part2:
            X += 10000000000000
            Y += 10000000000000

        # Aa1 + Bb1 = X
        # Aa2 + Bb2 = Y
        # [a1 b1   [A  = [X
        #  a2 b2]   B]    Y]
        # Assume full rank
        det = a1 * b2 - b1 * a2
        assert det != 0
        # [d -b;
        #  -c a]
        A_num =  b2 * X - b1 * Y
        B_num = -a2 * X + a1 * Y
        if A_num % det == 0 and B_num % det == 0:
            A = A_num // det
            B = B_num // det
            ans += 3 * A + B
    return ans

print(solve(part2=False))
print(solve(part2=True))