from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
s, t = map(int, input().split())
s -= 1
t -= 1

dist = [-1] * n
dist[s] = 0

q = deque([s])

while q:
    v = q.popleft()
    for u in range(n):
        if g[v][u] == 1 and dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)

print(dist[t])
