from collections import deque

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

q1 = deque(a1)
q2 = deque(a2)

cnt = 0
while cnt <= 1000000 and q1 and q2:
    cnt += 1
    a = q1.popleft()
    b = q2.popleft()
    if (a == 0 and b == 9) or (a > b and not (a == 9 and b == 0)):
        q1.append(a)
        q1.append(b)
    else:
        q2.append(a)
        q2.append(b)

if cnt >= 1000000:
    print("blin nichiya")
elif not q1:
    print("Nursik", cnt)
else:
    print("Boris", cnt)