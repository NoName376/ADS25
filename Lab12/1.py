import sys

input = sys.stdin.readline

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
order = [x - 1 for x in order]

active = [False] * n
ans = [0] * n

for step in range(n):
    k = order[step]
    active[k] = True
    row_k = dist[k]

    for i in range(n):
        row_i = dist[i]
        dik = row_i[k]
        for j in range(n):
            via = dik + row_k[j]
            if via < row_i[j]:
                row_i[j] = via

    best = 0
    for i in range(n):
        if not active[i]:
            continue
        row_i = dist[i]
        for j in range(n):
            if active[j] and row_i[j] > best:
                best = row_i[j]

    ans[step] = best

print("\n".join(map(str, ans)))
