from collections import defaultdict


n = int(input())
for _ in range(n):
    m = int(input())
    d = defaultdict(int)
    for _ in range(m):
        a, b = input().split()
        d[b] += 1
    tot = 1
    for e in d:
        tot *= d[e] + 1
    print(tot-1)