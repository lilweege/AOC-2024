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

FN = "input/17.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
regs, prog = s.split("\n\n")
regs = regs.split("\n")

instrs = list(map(int, prog.split(": ")[1].split(",")))
n = len(instrs)

def part1():
    A = int(regs[0].split(": ")[1])
    B = int(regs[1].split(": ")[1])
    C = int(regs[2].split(": ")[1])

    def combo_operand(x):
        if 0 <= x <= 3:
            return x
        if x == 4: return A
        if x == 5: return B
        if x == 6: return C
        assert x != 7
        assert 0

    out = []
    ip = 0
    while ip+1 < n:
        opcode = instrs[ip]
        operand = instrs[ip+1]

        if opcode == 0: # adv
            A = A // (2**combo_operand(operand))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo_operand(operand) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            out.append(combo_operand(operand) % 8)
        elif opcode == 6:
            B = A // (2**combo_operand(operand))
        elif opcode == 7:
            C = A // (2**combo_operand(operand))

        ip += 2

    return ",".join(map(str, out))


# 0: adv - performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
# 1: bxl - calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
# 2: bst - calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
# 3: jnz - does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
# 4: bxc - calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
# 5: out - calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
# 6: bdv - works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
# 7: cdv - works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
#  0: bst A      B = A & 0b111
#  2: bxl 1      B = B ^ 0b1
#  4: cdv B      C = A >> B
#  6: bxc A      B = B ^ C
#  8: bxl A      B = B ^ 0b100
# 10: adv 3      A = A >> 3
# 12: out B      write B & 0b111
# 14: jnz A, 0

# B = (A & 0b111) ^ 1
# C = A >> B
# B = B ^ C ^ 0b100
# A = A >> 3
# out B

def part2():
    import z3
    solver = z3.Optimize()
    A = z3.BitVec('A', 3*n+1)
    for i in range(n):
        curr_A = (A >> (3 * i))
        B = (curr_A & 0b111) ^ 1
        C = curr_A >> B
        B2 = B ^ C ^ 0b100
        solver.add((B2 & 0b111) == instrs[i])
    solver.minimize(A)

    if solver.check() == z3.sat:
        ans = solver.model()
        return ans[A].as_long()
    assert 0


def part2_better():
    q = [0]
    for result in reversed(instrs):
        b, q = q, []
        for curr_A in b:
            for A_low in range(8):
                next_A = (curr_A << 3) | A_low
                B = A_low ^ 1
                C = next_A >> B
                B = B ^ C ^ 0b100
                if (B & 0b111) == result:
                    q.append(next_A)
    return min(q)

print(part1())
# print(part2())
print(part2_better())