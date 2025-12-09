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
    u = next(it)
    v = next(it)
    g[u].append(v)


color = [0] * (n + 1)
parent = [-1] * (n + 1)
cycle = []
found_cycle = False

def dfs_find(v):
    global found_cycle, cycle
    color[v] = 1
    for to in g[v]:
        if found_cycle:
            return
        if color[to] == 0:
            parent[to] = v
            dfs_find(to)
        elif color[to] == 1:
            found_cycle = True
            path = []
            cur = v
            while cur != to:
                path.append(cur)
                cur = parent[cur]
            path.append(to)
            path.reverse()
            cycle = path
            return
    color[v] = 2

for v in range(1, n + 1):
    if not found_cycle and color[v] == 0:
        dfs_find(v)

if not found_cycle:
    print("YES")
    exit()

k = len(cycle)


vis_ver = [0] * (n + 1)
in_st_ver = [0] * (n + 1)
cur_ver = 0
has_cycle = False

def dfs_check(v, skip_u, skip_v):
    global has_cycle, cur_ver
    vis_ver[v] = cur_ver
    in_st_ver[v] = cur_ver

    for to in g[v]:
        if v == skip_u and to == skip_v:
            continue

        if vis_ver[to] != cur_ver:
            dfs_check(to, skip_u, skip_v)
            if has_cycle:
                return
        elif in_st_ver[to] == cur_ver:
            has_cycle = True
            return

    in_st_ver[v] = -1

for i in range(k):
    u = cycle[i]
    v = cycle[(i + 1) % k]

    cur_ver += 1
    has_cycle = False

    for start in range(1, n + 1):
        if vis_ver[start] != cur_ver:
            dfs_check(start, u, v)
            if has_cycle:
                break

    if not has_cycle:
        print("YES")
        exit()

print("NO")
