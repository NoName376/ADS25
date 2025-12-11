#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i].first >> a[i].second;
    }

    if (n == 1) {
        cout << 0 << '\n';
        return 0;
    }

    const long long INF = (long long)4e18;
    vector<long long> dist(n + 1, INF);
    vector<char> used(n + 1, 0);
    dist[1] = 0;

    for (int iter = 1; iter <= n; ++iter) {
        int v = -1;
        for (int i = 1; i <= n; ++i) {
            if (!used[i] && (v == -1 || dist[i] < dist[v])) v = i;
        }
        if (v == -1) break;
        used[v] = 1;

        long long xv = a[v].first, yv = a[v].second;
        for (int to = 1; to <= n; ++to) {
            if (used[to] || to == v) continue;
            long long xt = a[to].first, yt = a[to].second;
            long long dx = xv - xt, dy = yv - yt;
            long long d2 = dx * dx + dy * dy;

            long double root = sqrt((long double)d2);
            long long w = (long long)root;
            if (w * w < d2) ++w;

            long long nd = max(dist[v], w);
            if (nd < dist[to]) dist[to] = nd;
        }
    }

    cout << dist[n] << '\n';
    return 0;
}
