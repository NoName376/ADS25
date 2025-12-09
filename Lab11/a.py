import sys
import heapq


data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    exit(0)

it = iter(data)
n = next(it)
m = next(it)

start = [[] for _ in range(n + 2)]
end = [[] for _ in range(n + 2)]
costs = [0] * m

for idx in range(m):
    l = next(it)
    r = next(it)
    c = next(it)
    costs[idx] = c
    start[l].append(idx)
    end[r].append(idx)

heap = []
removed = [False] * m
answer = 0

for pos in range(1, n):

    for idx in end[pos]:
        removed[idx] = True

    for idx in start[pos]:
        heapq.heappush(heap, (costs[idx], idx))


    while heap and removed[heap[0][1]]:
        heapq.heappop(heap)

    min_cost, _ = heap[0]
    answer += min_cost

print(answer)
