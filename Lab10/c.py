n, m = map(int, input().split())

if n == m:
    print(0)
    exit(0)
path = [m]
cur = m

while cur != n:
    if cur < n:
        cur += 1
    else:
        if cur % 2 == 1:
            cur += 1
        else:
            cur //= 2
    path.append(cur)


path.reverse()

result = path[1:]

print(len(result))
if result:
    print(*result)
