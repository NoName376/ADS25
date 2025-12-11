import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

R, M, P, G = map(int, input().split())

INF = 10**18

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    h = [(0, start)]
    while h:
        d, v = heapq.heappop(h)
        if d != dist[v]:
            continue
        for to, w in g[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(h, (nd, to))
    return dist

distR = dijkstra(R)
distM = dijkstra(M)
distP = dijkstra(P)

ans = INF


if distR[M] < INF and distM[P] < INF and distP[G] < INF:
    ans = min(ans, distR[M] + distM[P] + distP[G])


if distR[P] < INF and distP[M] < INF and distM[G] < INF:
    ans = min(ans, distR[P] + distP[M] + distM[G])

print(ans if ans < INF else -1)
