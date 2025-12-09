#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) {
        return 0;
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;import sys
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

# 1) Находим компоненты и минимальную вершину в каждой (корень)
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

# 2) Строим дерево от каждого корня, считаем детей
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

# 3) Считаем BigFam
ans = 0
for v in range(1, n + 1):
    if parent[v] == 0:  # корень компоненты
        ans += 1
    else:
        if children[v] > children[parent[v]]:
            ans += 1

print(ans)

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<char> is_red(n + 1, false);
    int red_count = 0;

    while (q--) {
        int t, v;
        cin >> t >> v;
        if (t == 1) {
            if (!is_red[v]) {
                is_red[v] = true;
                ++red_count;
            }
        } else { // t == 2
            if (red_count == 0) {
                cout << -1 << '\n';
                continue;
            }

            vector<int> dist(n + 1, -1);
            queue<int> qu;
            dist[v] = 0;
            qu.push(v);
            int ans = -1;

            while (!qu.empty()) {
                int u = qu.front();
                qu.pop();

                if (is_red[u]) {
                    ans = dist[u];
                    break;
                }

                for (int to : adj[u]) {
                    if (dist[to] == -1) {
                        dist[to] = dist[u] + 1;
                        qu.push(to);
                    }
                }
            }

            cout << ans << '\n';
        }
    }

    return 0;
}