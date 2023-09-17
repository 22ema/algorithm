
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


N, M = map(int, input().split(' '))
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
points = list()

def check(a_x, a_y, b_x, b_y, x, y):
    if a_x + x < 0 or a_y + y <0 or a_x+ x >= N or a_y + y >= M:
        if b_x+ x < 0 or b_y + y < 0 or b_x+ x >=N or b_y + y >= M:
            return False
        else:
            return True
    elif b_x+ x < 0 or b_y + y < 0 or b_x+ x >=N or b_y + y >= M:
        if a_x+ x < 0 or a_y + y <0 or a_x+ x >= N or a_y + y >= M:
            return False
        else:
            return True


def solution(a_x, a_y, b_x, b_y, count):
    if count == 11:
        return -1

    for i in range(0, 4):
        if check(a_x, a_y, b_x, b_y, dx[i], dy[i]):
            return count + 1
    visited[a_x][a_y] = True
    visited[b_x][b_y] = True 
    for i in range(0, 4):
        if board[a_x+dx[i]] == '#' or board[a_x+dx[i]] == '#':
            solution(a_x, a_y, b_x+dx[i], b_y+dy[i], count+1)
            continue
        if board[b_x+dx[i]] == '#' or board[b_x+dx[i]] == '#':
            solution(a_x+dx[i], a_y+dy[i], b_x, b_y, count+1)
            continue
        solution(a_x+dx[i], a_y+dy[i], b_x+dx[i], b_y+dy[i], count+1)

for i in range(0, N):
    for j in range(0, M):
        if board[i][j] == 'o':
            points.append([i, j])

answers = solution(points[0][0], points[0][1], points[1][0], points[1][1], 0)
print(answers)