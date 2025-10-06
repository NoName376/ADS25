from collections import deque

n = int(input())
a = list(map(int, input().split()))
res = []
stack = deque()

for v in a:
    while stack and stack[-1] > v:
        stack.pop()
    res.append(stack[-1] if stack else -1)
    stack.append(v)

print(' '.join(map(str, res)))