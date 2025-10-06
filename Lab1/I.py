from collections import deque

n = int(input())
s = input().strip()

S = deque()
K = deque()

for i, ch in enumerate(s):
    if ch == 'S':
        S.append(i)
    else:
        K.append(i)

while S and K:
    idS = S.popleft()
    idK = K.popleft()

    if idS < idK:
        S.append(idS + n)
    else:
        K.append(idK + n)

print("KATSURAGI" if not S else "SAKAYANAGI")