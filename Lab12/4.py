import sys
sys.setrecursionlimit(2000)

data = sys.stdin.read().split()
if not data:
    exit()
it = iter(data)
n = int(next(it))

if n == 1:
    print(0)
    exit()

xs = [0]*n
ys = [0]*n
for i in range(n):
    xs[i] = int(next(it))
    ys[i] = int(next(it))

inf = 10**30
dist = [inf]*n
dist[0] = 0
vis = [0]*n

for _ in range(n):
    u = -1
    mv = inf
    for i in range(n):
        if not vis[i] and dist[i] < mv:
            mv = dist[i]
            u = i
    if u == -1 or mv == inf:
        break
    vis[u] = 1
    if u == n-1:
        print(mv)
        exit()
    ux = xs[u]
    uy = ys[u]
    for v in range(n):
        if not vis[v]:
            w = abs(ux - xs[v]) + abs(uy - ys[v])
            nd = mv if mv > w else w
            if nd < dist[v]:
                dist[v] = nd
