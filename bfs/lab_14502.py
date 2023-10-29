
from collections import deque
import copy

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, input().split(' '))
result = 0
MAP = list()
for _ in range(N):
    field = list(map(int, input().split(' ')))
    MAP.append(field)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for n in range(N):
        for m in range(M):
            if MAP[n][m] == 0:
                MAP[n][m] = 1
                make_wall(count+1)
                MAP[n][m] = 0

def bfs():
    queue = deque()
    test_map = copy.deepcopy(MAP)
    for n in range(N):
        for m in range(M):
            if test_map[n][m] == 2:
                queue.append((n, m))
    while queue:
        n, m = queue.popleft()
        for i in range(4):
            d_n = n + d[i][0]
            d_m = m + d[i][1]
            if 0 <= d_n < N and 0 <= d_m <M:
                if test_map[d_n][d_m] == 0:
                    test_map[d_n][d_m] = 2
                    queue.append((d_n, d_m))

    global result
    count = 0
    for n in range(N):
        for m in range(M):
            if test_map[n][m] == 0:
                count += 1
    result = max(result, count)

make_wall(0)
print(result)
