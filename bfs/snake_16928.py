from collections import deque

# N, M = map(int, input().split(' '))

# after = list(range(101))
# dist = [-1] * 101

# for _ in range(N+M):
#     x, y = map(int, input().split(' '))
#     after[x] = y

# dist[1] = 0
# q = deque()
# q.append(1)
# while q:
#     x = q.popleft()
#     ## 주사위 굴리기
#     for i in range(1, 6+1):
#         # 주사위 굴려서 나온 수만큼 더하기
#         y = x + i
#         ## 종료
#         if y > 100:
#             continue
#         ## after[y]가 해당 칸에서 어디로 갈지를 나타내는 것이니 거기로 날려버리기 그리고 거기에 해당하는 dist를 넣으면 그 dist가 최소인 것임.
#         y = after[y]
#         if dist[y] == -1:
#             dist[y] = dist[x] + 1
#             q.append(y)
# print(dist[100])


N, M = map(int, input().split(' '))
after = [i for i in range(0, 101)]
dist = [-1] * 101

for _ in range(N+M):
    x, y = map(int, input().split(' '))
    after[x] = y

dist[1] = 0
dq = deque()
dq.append(1)
while dq:
    x = dq.popleft()
    for i in range(1, 7):
        y = x + i
        if y > 100:
            continue
        y = after[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            dq.append(y)
print(dist[100])
































