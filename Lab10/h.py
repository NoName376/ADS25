import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def dfs(si, sj):
    stack = [(si, sj)]
    visited[si][sj] = True
    while stack:
        i, j = stack.pop()
        # 4 направления
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and grid[ni][nj] == '1':
                    visited[ni][nj] = True
                    stack.append((ni, nj))

islands = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and not visited[i][j]:
            islands += 1
            dfs(i, j)

print(islands)