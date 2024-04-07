from collections import deque
# 각 조합에 대한
N, V = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
virus_list = list()
answer = 10000000
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] = '_'
        elif board[i][j] == 1:
            board[i][j] = '-'
        elif board[i][j] == 2:
            virus_list.append((i, j))
            board[i][j] = '*'

virus_comb_list = list()
def combination(start, curr, num):
    if len(curr) == num:
        virus_comb_list.append(curr[:])
    for i in range(start, len(virus_list)):
        curr.append(virus_list[i])
        combination(i+1, curr, num)
        curr.pop()
def bfs(virus_comb):
    global answer
    que = deque()
    for x, y in virus_comb:
        que.append((x, y, 0))
    test_map = [board[i][:] for i in range(N)]
    max_count = 0
    while que:
        x, y, count = que.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_count = count + 1
            if 0 <= next_x < N and 0 <= next_y < N:
                if test_map[next_x][next_y] == '_':
                    test_map[next_x][next_y] = next_count
                    max_count = max(max_count, next_count)
                    que.append((next_x, next_y, next_count))
                elif test_map[next_x][next_y] == '*':
                    test_map[next_x][next_y] = next_count
                    que.append((next_x, next_y, next_count))
    for i in range(N):
        for j in range(N):
            if test_map[i][j] == '_':
                return
    answer = min(answer, max_count)
    return

combination(0, [], V)

for virus_comb in virus_comb_list:
    bfs(virus_comb)
if answer == 10000000:
    print(-1)
else:
    print(answer)