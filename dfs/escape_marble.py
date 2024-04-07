from collections import deque
# 각 조합에 대한
N, M = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
board = [list(input()) for _ in range(N)]
visited = set()
red_stone = None
blue_stone = None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_stone = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue_stone = [i, j]
            board[i][j] = '.'


def move(stone, dx, dy):
    comp = False
    move = 0
    while True:
        stone[0] += dx
        stone[1] += dy
        move += 1
        if 0 <= stone[0] < N and 0 <= stone[1] < M:
            if board[stone[0]][stone[1]] == 'O':
                comp = True
                return stone, comp, move
            if board[stone[0]][stone[1]] == '#':
                break
    stone[0] -= dx
    stone[1] -= dy
    move -= 1
    return stone, comp, move

def bfs(blue, red):
    que = deque()
    count = 1
    que.append((blue, red, count))
    visited.add((blue[0], blue[1], red[0], red[1]))
    while que:
        curr_blue, curr_red, count = que.popleft()
        if count > 10:
            break
        for i in range(4):
            next_blue, blue_comp, blue_count = move(curr_blue[:], dx[i], dy[i])
            next_red, red_comp, red_count = move(curr_red[:], dx[i], dy[i])
            if blue_comp == True:
                continue
            elif red_comp == True:
                return 1
            else:
                if next_blue == next_red:
                    if red_count > blue_count:
                        next_red[0] -= dx[i]
                        next_red[1] -= dy[i]
                    elif blue_count > red_count:
                        next_blue[0] -= dx[i]
                        next_blue[1] -= dy[i]
                if (next_blue[0], next_blue[1], next_red[0], next_red[1]) in visited:
                    continue
                que.append((next_blue[:], next_red[:], count+1))
                visited.add((next_blue[0], next_blue[1], next_red[0], next_red[1]))
    return 0
print(bfs(blue_stone, red_stone))