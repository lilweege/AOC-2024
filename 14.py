from collections import Counter, defaultdict
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial
from dataclasses import dataclass
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/14.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
# X = 11
# Y = 7
X = 101
Y = 103

@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int
    def update(self):
        self.px = (self.px + self.vx) % X
        self.py = (self.py + self.vy) % Y

orig_robots = []
for l in s.split("\n"):
    a, b = l.split(" ")
    px, py = map(int, a[2:].split(","))
    vx, vy = map(int, b[2:].split(","))
    orig_robots.append(Robot(px, py, vx, vy))


def part1():
    robots = deepcopy(orig_robots)
    for _ in range(100):
        for robot in robots:
            robot.update()
    positions = defaultdict(int)
    for robot in robots:
        positions[(robot.px, robot.py)] += 1

    cnt1 = cnt2 = cnt3 = cnt4 = 0
    for y in range(Y//2):
        for x in range(X//2):
            cnt1 += positions[(x, y)]
    for y in range(Y//2+1, Y):
        for x in range(X//2):
            cnt2 += positions[(x, y)]
    for y in range(Y//2):
        for x in range(X//2+1, X):
            cnt3 += positions[(x, y)]
    for y in range(Y//2+1, Y):
        for x in range(X//2+1, X):
            cnt4 += positions[(x, y)]
    ans = cnt1 * cnt2 * cnt3 * cnt4
    return ans


def part2():
    robots = deepcopy(orig_robots)
    t = 0
    while True:
        t += 1
        ok = True
        positions = set()
        for robot in robots:
            robot.update()
            if ok:
                if (robot.px, robot.py) in positions:
                    ok = False
                positions.add((robot.px, robot.py))

        if ok:
            # for y in range(Y):
            #     for x in range(X):
            #         c = '1' if (x, y) in positions else '.'
            #         print(c, end="")
            #     print()
            # print(t)
            return t

print(part1())
print(part2())