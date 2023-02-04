import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(m)]

que = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0

for i in range(m):
    for j in range(n):
        if tomatos[i][j] == 1:
            que.append([i, j])

while que:
    x, y = que.popleft()

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < m and 0 <= ny < n and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = tomatos[x][y] + 1
            que.append([nx, ny])

for list in tomatos:
    for tomato in list:
        if tomato == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(list))

print(ans-1)