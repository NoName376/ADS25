#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> dist(n, vector<long long>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> dist[i][j];

    vector<int> order(n);
    for (int i = 0; i < n; ++i) {
        cin >> order[i];
        --order[i];
    }

    vector<int> active(n, 0);
    vector<long long> ans(n);

    for (int step = 0; step < n; ++step) {
        int k = order[step];
        active[k] = 1;
        auto &row_k = dist[k];

        for (int i = 0; i < n; ++i) {
            auto &row_i = dist[i];
            long long dik = row_i[k];
            for (int j = 0; j < n; ++j) {
                long long via = dik + row_k[j];
                if (via < row_i[j]) row_i[j] = via;
            }
        }

        long long best = 0;
        for (int i = 0; i < n; ++i) {
            if (!active[i]) continue;
            auto &row_i = dist[i];
            for (int j = 0; j < n; ++j) {
                if (active[j] && row_i[j] > best) best = row_i[j];
            }
        }

        ans[step] = best;
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
