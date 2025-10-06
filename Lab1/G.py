n = int(input())
limit = 100000

prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

v = [i for i in range(2, limit + 1) if prime[i]]

cnt = 0
for i in range(2, limit + 1):
    if prime[i]:
        cnt += 1
    if cnt == n:
        print(v[i - 1])
        break