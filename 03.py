from collections import Counter
from itertools import pairwise
import re

FN = "input/03.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

ans1 = sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", s))
print(ans1)

ans2 = 0
yes = True
for do, dont, a, b in re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", s):
    if do:
        yes = True
    elif dont:
        yes = False
    elif yes:
        ans2 += int(a) * int(b)
print(ans2)
