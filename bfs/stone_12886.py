
'''
돌의 총 개수가 3의 배수가 아니면 만들 수 없다.
'''

from collections import deque

A, B, C = map(int, input().split(' '))
total = A + B + C
visited = [[False] * (total+1) for _ in range(total + 1)]

def bfs():
    global A, B, C, total, visited
    q = deque()
    q.append((A, B))
    while q:
        a, b = q.popleft()
        c = total - (a + b)
        visited[a][b] = True
        if a == b == c:
            print(1)
            return
        for x, y in (a, b), (b, c), (c, a):
            if x < y:

                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            else:
                continue
            c = total - (x + y)
            min_x = min(x, y, c)
            max_y = max(x, y, c)
            if visited[min_x][max_y] == True:
                continue
            else:
                q.append((min_x, max_y))
                visited[min_x][max_y] = True
    print(0)

if (A+B+C) % 3 != 0:
    print(0)
else:
    bfs()