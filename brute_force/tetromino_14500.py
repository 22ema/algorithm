dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

## numbers[0] = 세로, numbers[1] = 가로
numbers = list(map(int, input().split()))
tetromino = [list(map(int, input().split())) for _ in range(0, numbers[0])]
visited = [[False] * numbers[1] for _ in range(0, numbers[0])]

def solution(x, y, sum, cnt):
    if cnt == 4:
        global ans
        if ans < sum:
            ans = sum
        return
    if x < 0 or y < 0 or x >= numbers[0] or y >= numbers[1]:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    for k in range(4):
        solution(x+dx[k], y+dy[k], sum+tetromino[x][y], cnt+1)
    visited[x][y] = False

ans = 0
for i in range(0, numbers[0]):
    for j in range(0, numbers[1]):
        solution(i, j, 0, 0)
        if j+2 < numbers[1]:
            result = tetromino[i][j] + tetromino[i][j+1] + tetromino[i][j+2]
            if i+1 < numbers[0]:
                result2 = result + tetromino[i+1][j+1]
                if ans < result2:
                    ans = result2
            if i-1 >= 0:
                result2 = result + tetromino[i-1][j+1]
                if ans < result2:
                    ans = result2
        if i+2 < numbers[0]:
            result = tetromino[i][j] + tetromino[i+1][j] + tetromino[i+2][j]
            if j+1 < numbers[1]:
                result2 = result + tetromino[i+1][j+1]
                if ans < result2:
                    ans = result2
            if j-1 >= 0:
                result2 = result + tetromino[i+1][j-1]
                if ans < result2:
                    ans = result2
print(ans)