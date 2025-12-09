import sys
from collections import deque


data = list(map(int, sys.stdin.read().split()))
if not data:
    exit(0)

it = iter(data)
n = next(it)
m = next(it)


g = [[] for _ in range(n + 1)]
for _ in range(m):
    x = next(it)
    y = next(it)
    g[x].append(y)
    g[y].append(x)

s = next(it)
f = next(it)


visited = [False] * (n + 1)
q = deque([s])
visited[s] = True

while q:
    v = q.popleft()
    if v == f:
        print("YES")
        exit(0)
    for to in g[v]:
        if not visited[to]:
            visited[to] = True
            q.append(to)

print("NO")


