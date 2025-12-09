n = int(input())
a = list(map(int, input().split()))

mn = min(a)
s = sum(a)


print(s + (n - 2) * mn)
