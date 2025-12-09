import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

it = iter(data)
n = next(it)
m = next(it)

g = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    u = next(it)
    v = next(it)
    g[u].append(v)
    indeg[v] += 1

q = deque()


for v in range(1, n + 1):
    if indeg[v] == 0:
        q.append(v)

order = []

while q:
    v = q.popleft()
    order.append(v)
    for to in g[v]:
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)

if len(order) != n:
    print("Impossible")
else:
    print("Possible")
    print(*order)
