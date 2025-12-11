#include <bits/stdc++.h>
using namespace std;

const long long INF = (long long)1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }

    int R, M, P, G;
    cin >> R >> M >> P >> G;

    auto dijkstra = [&](int start) {
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        dist[start] = 0;
        pq.push({0, start});
        while (!pq.empty()) {
            auto [d, v] = pq.top();
            pq.pop();
            if (d != dist[v]) continue;
            for (auto [to, w] : g[v]) {
                long long nd = d + w;
                if (nd < dist[to]) {
                    dist[to] = nd;
                    pq.push({nd, to});
                }
            }
        }
        return dist;
    };

    vector<long long> distR = dijkstra(R);
    vector<long long> distM = dijkstra(M);
    vector<long long> distP = dijkstra(P);

    long long ans = INF;


    if (distR[M] < INF && distM[P] < INF && distP[G] < INF) {
        ans = min(ans, distR[M] + distM[P] + distP[G]);
    }


    if (distR[P] < INF && distP[M] < INF && distM[G] < INF) {
        ans = min(ans, distR[P] + distP[M] + distM[G]);
    }

    if (ans >= INF) cout << -1 << "\n";
    else cout << ans << "\n";

    return 0;
}
