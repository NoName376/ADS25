from collections import deque

n = int(input())
for _ in range(n):
    x = int(input())
    res = [-1] * x
    dq = deque(range(x))
    for cur in range(1, x + 1):
        dq.rotate(-(cur))
        pos = dq.popleft()
        res[pos] = cur
    print(' '.join(map(str, res)))