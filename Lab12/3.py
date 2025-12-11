import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

air_adj = [[] for _ in range(n + 1)]
is_air = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    air_adj[u].append(v)
    air_adj[v].append(u)
    is_air[u][v] = True
    is_air[v][u] = True

INF = 10**9


dist_air = [INF] * (n + 1)
q = deque([1])
dist_air[1] = 0

while q:
    v = q.popleft()
    for to in air_adj[v]:
        if dist_air[to] == INF:
            dist_air[to] = dist_air[v] + 1
            q.append(to)


dist_road = [INF] * (n + 1)
q = deque([1])
dist_road[1] = 0

while q:
    v = q.popleft()
    for to in range(1, n + 1):
        if to == v:
            continue
        if not is_air[v][to] and dist_road[to] == INF:
            dist_road[to] = dist_road[v] + 1
            q.append(to)

if dist_air[n] == INF or dist_road[n] == INF:
    print(-1)
else:
    print(max(dist_air[n], dist_road[n]))
