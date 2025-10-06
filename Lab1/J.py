from collections import deque

dq = deque()

while True:
    line = input().split()
    if not line:
        continue
    c = line[0]
    if c == '+':
        dq.appendleft(int(line[1]))
    elif c == '-':
        dq.append(int(line[1]))
    elif c == '*':
        if not dq:
            print("error")
        else:
            print(dq[0] + dq[-1])
            if len(dq) >= 2:
                dq.popleft()
                dq.pop()
            else:
                dq.popleft()
    else:
        break