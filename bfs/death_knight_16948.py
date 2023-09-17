from collections import deque


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, +2, -1, 1]
N = int(input())
r1, c1, r2, c2 = map(int, input().split(' '))

dist = [[-1]*N for _ in range(N)]

dq = deque()
dq.append((r1, c1))
dist[r1][c1] = 0
while dq:
    x, y = dq.popleft()
    for i in range(0, 6):
        a_x = x + dx[i]
        a_y = y + dy[i]
        if a_x < 0 or a_y < 0 or a_x >=N or a_y >= N:
            continue
        if x == r2 and y == c2:
            continue
        if dist[a_x][a_y] == -1:
            dist[a_x][a_y] = dist[x][y] + 1
            dq.append((a_x, a_y))
print(dist[r2][c2])