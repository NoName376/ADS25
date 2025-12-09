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

iterator = iter(input_data)

try:
    n = int(next(iterator))
    m = int(next(iterator))
    c_big = int(next(iterator))
    c_small = int(next(iterator))
except StopIteration:
    exit(0)

edges = []

for _ in range(m):
    road_type = next(iterator)
    u = int(next(iterator))
    v = int(next(iterator))
    length = int(next(iterator))

    cost = 0
    if road_type == "big":
        cost = length * c_big
    elif road_type == "small":
        cost = length * c_small
    else:  # both
        cost = length * min(c_big, c_small)

    edges.append((cost, u, v))


edges.sort(key=lambda x: x[0])

dsu = DSU(n)
total_cost = 0
edges_count = 0

for cost, u, v in edges:
    if dsu.unite(u, v):
        total_cost += cost
        edges_count += 1
        if edges_count == n - 1:
            break

print(total_cost)
