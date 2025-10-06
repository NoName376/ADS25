from collections import deque
import math

n = int(input())
li = list(map(int, input().split()))
a = int(input())

ind = 0
b_dist = math.fabs(li[0] - a)

for i in range(n):
    dif = math.fabs(li[i] - a)
    if(dif < b_dist):
        ind = i
        b_dist = dif


print(ind)