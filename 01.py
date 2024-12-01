from collections import Counter

FN = "input/01.txt"
# FN = "sample.txt"
FILE = open(FN, "r")

s = FILE.read().strip()
aa = []
bb = []
for l in s.split("\n"):
    a, b = map(int, l.split())
    aa.append(a)
    bb.append(b)
ans1 = sum(abs(b-a) for a, b in zip(sorted(aa), sorted(bb)))
print(ans1)

cnt = Counter(bb)
ans2 = sum(a * cnt[a] for a in aa)
print(ans2)
