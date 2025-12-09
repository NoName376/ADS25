import sys



input_data = sys.stdin.read().split()
if not input_data:
    exit(0)

iterator = iter(input_data)
try:
    n = int(next(iterator))
except StopIteration:
    exit(0)


adj = []
for _ in range(n):
    row = []
    for _ in range(n):
        row.append(int(next(iterator)))
    adj.append(row)


INF = float('inf')
min_e = [INF] * n
used = [False] * n

min_e[0] = 0
total_cost = 0

for _ in range(n):
    v = -1

    for j in range(n):
        if not used[j]:
            if v == -1 or min_e[j] < min_e[v]:
                v = j

    if v == -1 or min_e[v] == INF:
        break

    used[v] = True
    total_cost += min_e[v]


    for to in range(n):
        if not used[to]:
            if adj[v][to] < min_e[to]:
                min_e[to] = adj[v][to]

print(total_cost)
