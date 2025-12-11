import sys
sys.setrecursionlimit(2000)

data = sys.stdin.read().split()
if not data:
    exit()

it = iter(data)
try:
    n = int(next(it))
except StopIteration:
    exit()

edges = []
M = 100000

for i in range(n):
    for j in range(n):
        w = int(next(it))
        if w != M:
            edges.append((i, j, w))

dist = [0] * n
parent = [-1] * n
x = -1

for _ in range(n):
    x = -1
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            x = v

if x == -1:
    print("NO")
    exit()

y = x
for _ in range(n):
    y = parent[y]

path = []
cur = y
while True:
    path.append(cur)
    if cur == y and len(path) > 1:
        break
    cur = parent[cur]

path.reverse()

print("YES")
print(len(path))
print(*(i + 1 for i in path))
