from collections import deque
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
def maze_runner(N, M, maze, visited_list):
    q = deque()
    q.append([0, 0])
    while q:
        index = q.popleft()
        for i in range(0, 4):
            xx = x[i] + index[0]
            yy = y[i] + index[1]
            if xx >= 0 and yy >= 0 and xx < N and yy < M:
                if visited_list[xx][yy] == 0 and maze[xx][yy] == '1':
                    q.append([xx, yy])
                    visited_list[xx][yy] = visited_list[index[0]][index[1]] + 1

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    maze = list()
    visited_list = [[0] * M for _ in range(N)]
    for i in range(0, N):
        maze_comp = list(input())
        maze.append(maze_comp)
    maze_runner(N, M, maze, visited_list)
    print(visited_list[N-1][M-1]+1)