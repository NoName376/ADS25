import sys

sys.setrecursionlimit(200000)


class DSU:

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False




input_data = sys.stdin.read().split()
if not input_data:
    exit(0)

try:
    n = int(input_data[0])
    m = int(input_data[1])
except IndexError:
    exit(0)


adj = [[] for _ in range(n + 1)]


edge_data = input_data[2:]

for i in range(0, m * 2, 2):
    u = int(edge_data[i])
    v = int(edge_data[i + 1])
    adj[u].append(v)
    adj[v].append(u)


dsu = DSU(n)
is_present = [False] * (n + 1)
results = []
current_components = 0


for i in range(n, 0, -1):
    v = i

    is_present[v] = True
    current_components += 1


    for u in adj[v]:
        if is_present[u]:

            if dsu.unite(u, v):
                current_components -= 1


    results.append(current_components)


results.pop()


results.reverse()
results.append(0)

sys.stdout.write('\n'.join(map(str, results)) + '\n')
