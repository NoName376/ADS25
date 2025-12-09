import sys
sys.setrecursionlimit(10**7)

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

it = iter(data)
n = next(it)
m = next(it)

g = [[] for _ in range(n + 1)]
for _ in range(m):
    x = next(it)
    y = next(it)
    g[x].append(y)
    g[y].append(x)


visited = [False] * (n + 1)
roots = []

for v in range(1, n + 1):
    if not visited[v]:
        stack = [v]
        visited[v] = True
        minv = v
        while stack:
            u = stack.pop()
            if u < minv:
                minv = u
            for nei in g[u]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        roots.append(minv)


children = [0] * (n + 1)
parent = [0] * (n + 1)
visited2 = [False] * (n + 1)

for r in roots:
    if visited2[r]:
        continue
    stack = [(r, 0)]
    visited2[r] = True
    parent[r] = 0
    while stack:
        u, p = stack.pop()
        for nei in g[u]:
            if not visited2[nei]:
                visited2[nei] = True
                parent[nei] = u
                children[u] += 1
                stack.append((nei, u))


ans = 0
for v in range(1, n + 1):
    if parent[v] == 0:
        ans += 1
    else:
        if children[v] > children[parent[v]]:
            ans += 1

print(ans)
