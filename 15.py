from collections import Counter, defaultdict, deque
from itertools import pairwise
from copy import deepcopy
from functools import cache, partial
from dataclasses import dataclass
import re

# import sys
# sys.setrecursionlimit(9999)

FN = "input/15.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()

def part1():
    g, l = s.split("\n\n")
    g = [list(r) for r in g.split("\n")]
    n, m = len(g), len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j] == '@':
                g[i][j] = '.'
                start = i, j

    l = l.replace("\n", "")

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    pi, pj = start
    for c in l:
        if c == '>':
            d = 0
        elif c == 'v':
            d = 1
        elif c == '<':
            d = 2
        elif c == '^':
            d = 3
        else:
            assert 0

        di, dj = dirs[d]
        ni, nj = pi + di, pj + dj
        if g[ni][nj] == '.':
            pi, pj = ni, nj
            continue
        elif g[ni][nj] == '#':
            continue
        else:
            fi, fj = pi + di, pj + dj
            assert g[fi][fj] == 'O'
            while True:
                ni += di
                nj += dj
                if g[ni][nj] == '#':
                    break
                elif g[ni][nj] == '.':
                    g[ni][nj] = 'O'
                    g[fi][fj] = '.'
                    pi, pj = fi, fj
                    break

    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'O':
                ans += 100*i+j
    return ans


def part2():
    g, l = s.split("\n\n")
    g = [list(r) for r in g.split("\n")]
    n, m = len(g), len(g[0])


    l = l.replace("\n", "")


    m *= 2
    dbl_g = [[' '] * m for _ in range(n)]
    for i in range(n):
        for j in range(m//2):
            if g[i][j] == '@':
                g[i][j] = '.'
                start = i, 2*j
            if g[i][j] == 'O':
                dbl_g[i][j*2] = '['
                dbl_g[i][j*2+1] = ']'
            else:
                dbl_g[i][j*2] = dbl_g[i][j*2+1] = g[i][j]
    g = dbl_g

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def get_pair(i, j):
        c = g[i][j]
        if c == '[': return i, j+1
        if c == ']': return i, j-1
        assert 0
    def other(c):
        if c == '[': return ']'
        if c == ']': return '['
        assert 0

    def print_grid():
        print(pi, pj)
        for i in range(n):
            for j in range(m):
                if (i, j) == (pi, pj):
                    print('@', end="")
                else:
                    print(g[i][j], end="")
            print()

    pi, pj = start
    for c in l:
        if c == '>':
            d = 0
        elif c == 'v':
            d = 1
        elif c == '<':
            d = 2
        elif c == '^':
            d = 3
        else:
            assert 0

        di, dj = dirs[d]
        ni, nj = pi + di, pj + dj
        if g[ni][nj] == '.':
            pi, pj = ni, nj
            continue
        elif g[ni][nj] == '#':
            continue
        else:
            if dj != 0:
                fi, fj = pi + di, pj + dj
                assert g[ni][nj] in '[]'
                first = g[ni][nj]
                step = 0
                while True:
                    if g[ni][nj] == '#':
                        break
                    elif g[ni][nj] == '.':
                        for i in range(step):
                            g[fi][fj+i*dj] = other(g[fi][fj+i*dj])
                        g[ni][nj] = other(first)
                        g[fi][fj] = '.'
                        pi, pj = fi, fj
                        break
                    else:
                        assert g[ni][nj] in '[]'
                        ni += 2*di
                        nj += 2*dj
                        step += 2
            else:
                assert g[ni][nj] in '[]'
                q = deque([(ni, nj)])
                vis = set()
                ok = True
                while q:
                    ni1, nj1 = q.popleft()
                    if (ni1, nj1) in vis:
                        continue
                    ni2, nj2 = get_pair(ni1, nj1)
                    assert g[ni1][nj1] in '[]'
                    assert g[ni2][nj2] in '[]'
                    vis.add((ni1, nj1))
                    vis.add((ni2, nj2))

                    nni1, nnj1 = ni1+di, nj1+dj
                    if g[nni1][nnj1] in '[]':
                        q.append((nni1, nnj1))
                    elif g[nni1][nnj1] == '#':
                        ok = False
                        break
                    nni2, nnj2 = ni2+di, nj2+dj
                    if g[nni2][nnj2] in '[]':
                        q.append((nni2, nnj2))
                    elif g[nni2][nnj2] == '#':
                        ok = False
                        break
                if ok:
                    shifted = {(i, j): (i+di, j+dj) for i, j in vis}
                    ng = deepcopy(g)
                    ni1, nj1 = ni, nj
                    ni2, nj2 = get_pair(ni1, nj1)
                    for i, j in vis:
                        ng[i][j] = '.'
                    for (oi, oj), (ni, nj) in shifted.items():
                        ng[ni][nj] = g[oi][oj]
                    g = ng
                    pi, pj = pi + di, pj + dj

    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '[':
                ans += 100*i+j
    return ans


print(part1())
print(part2())