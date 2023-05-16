# ## 1차 나의 풀이
# def peel_off_stiker(stikers, visited, number, answer):
#     plus = [(1, 0),
#         (0, 1),
#         (-1, 0),
#         (0, -1)
#         ]
#     finished = 0
#     max = 0
#     rows = 0
#     cols = 0
#     for i in range(0, 2):
#         for j in range(0, number):
#             if visited[i][j] == False: finished = -1
    
#     if finished == 0:
#         return answer
    
#     for i in range(0, 2):
#         for j in range(0, number):
#             if visited[i][j] is True: continue
#             if max <= stikers[i][j]:
#                 max = stikers[i][j]
#                 rows = j
#                 cols = i
#     visited[cols][rows] = True
#     for i, j in plus:
#         cols_ = cols + i
#         rows_ = rows + j
#         if cols_ < 0 or rows_ < 0 or cols_ >= 2 or rows_ >= number: 
#             pass
#         else:
#             visited[cols_][rows_] = True
#     answer += max
#     answer = peel_off_stiker(stikers, visited, number, answer)
#     return answer


# if __name__ == "__main__":
#     test_case = int(input())
#     for i in range(0, test_case):
#         answer = 0
#         number = int(input())
#         stikers = list()
#         for j in range(0, 2):
#             stiker = list(map(int, input().split()))
#             stikers.append(stiker)
#         visited = [[False]*number, [False]*number]
#         answer = peel_off_stiker(stikers, visited, number, answer)
#         print(answer)
## 참고 코드
# t = int(input())
# for i in range(t):
#     s = list()
#     n = int(input())
#     for k in range(2):
#         s.append(list(map(int, input().split())))
#     for j in range(1, n):
#         if j == 1:
#             s[0][j] += s[1][j-1]
#             s[1][j] += s[0][j-1]
#         else:
#             s[0][j] += max(s[1][j-1], s[1][j-2])
#             s[1][j] += max(s[0][j-1], s[0][j-2])
#     print(max(s[0][n-1], s[1][n-1]))

## 다시 한번 풀어봐야함

def peel_off_stiker(stikers, number):
    for i in range(1, number):
        if i == 1:
            stikers[1][i] += stikers[0][i-1]
            stikers[0][i] += stikers[1][i-1]
        else:
            stikers[0][i] += max(stikers[1][i-1], stikers[1][i-2])
            stikers[1][i] += max(stikers[0][i-1], stikers[0][i-2])
    return max(stikers[0][number-1], stikers[1][number-1])

if __name__ == "__main__":
    test_case = int(input())
    for i in range(0, test_case):
        answer = 0
        number = int(input())
        stikers = list()
        for j in range(0, 2):
            stiker = list(map(int, input().split()))
            stikers.append(stiker)
        answer = peel_off_stiker(stikers, number)
        print(answer)