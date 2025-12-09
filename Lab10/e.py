import sys


data = list(map(int, sys.stdin.read().split()))
if not data:
    exit(0)

it = iter(data)
n = next(it)
q = next(it)


adj = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        adj[i][j] = next(it)

out_lines = []
for _ in range(q):
    a = next(it) - 1
    b = next(it) - 1
    c = next(it) - 1

    if adj[a][b] and adj[a][c] and adj[b][c]:
        out_lines.append("YES")
    else:
        out_lines.append("NO")

sys.stdout.write("\n".join(out_lines))


