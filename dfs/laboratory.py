from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty = list()
wall_case = list()
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))

def combinations_(start, curr):
    if len(curr) == 3:
        wall_case.append(curr[:])
        return
    for i in range(start, len(empty)):
        curr.append(empty[i])
        combinations_(i+1, curr)
        curr.pop()

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

def dfs(x, y):
    visited[x][y] = True
    global count
    if board[x][y] == 0:
        count += 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if is_valid(next_x, next_y):
            if visited[next_x][next_y] == False and board[next_x][next_y] == 0:
                dfs(next_x, next_y)

combinations_(0, [])
# wall_case = combinations(empty, 3)
empty_count = len(empty) - 3
max_count = 0
for walls in wall_case:
    count = 0
    visited = [[False] * M for _ in range(N)]
    for wall in walls:
        board[wall[0]][wall[1]] = 1
    for i in range(0, N):
        for j in range(0, M):
            if board[i][j] == 2:
                dfs(i, j)
    if (empty_count - count) > max_count:
        max_count = empty_count - count
    for wall in walls:
        board[wall[0]][wall[1]] = 0
print(max_count)

## 먼저 맵을 만들자?