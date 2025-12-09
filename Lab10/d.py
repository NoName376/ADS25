from collections import deque
import sys

sys.setrecursionlimit(10**6)
data = list(map(int, sys.stdin.read().split()))
it = iter(data)

n = next(it)
m = next(it)
q = next(it)

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u = next(it)
    v = next(it)
    adj[u].append(v)
    adj[v].append(u)

is_red = [False] * (n + 1)
red_count = 0
out_lines = []

for _ in range(q):
    t = next(it)
    v = next(it)
    if t == 1:
        if not is_red[v]:
            is_red[v] = True
            red_count += 1
    else:
        if red_count == 0:
            out_lines.append("-1")
            continue

        dist = [-1] * (n + 1)
        dist[v] = 0
        dq = deque([v])
        ans = -1

        while dq:
            u = dq.popleft()
            if is_red[u]:
                ans = dist[u]
                break
            for to in adj[u]:
                if dist[to] == -1:
                    dist[to] = dist[u] + 1
                    dq.append(to)

        out_lines.append(str(ans))

sys.stdout.write("\n".join(out_lines))
