
def NMK(index,start_i, start_j, N, M, numbers_list, visited_list, selected_list, max, x, y):
    if index == len(selected_list):
        sum = 0
        for i in selected_list:
            sum += i
        if max < sum:
            max = sum
        return max
    for i in range(start_i, N):
        for j in range(start_j if start_i == i else 0, M):
            if visited_list[i][j] == True:
                continue
            check = True
            for k in range(0,4):
                xx = i + x[k]
                yy = j + y[k]
                if 0 <= xx < N and 0 <= yy < M:
                    if visited_list[xx][yy] == True:
                        check = False
            if check:
                visited_list[i][j] = True
                selected_list[index] = numbers_list[i][j]
                max = NMK(index+1, i, j, N, M, numbers_list, visited_list, selected_list, max, x, y)
                visited_list[i][j] = False
    return max
if __name__ == "__main__":
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]
    numbers = list(map(int, input().split()))
    numbers_list = [list(map(int, input().split())) for i in range(0, numbers[0])]
    visited_list = [[False] * numbers[1] for i in range(0, numbers[0])]
    selected_list = [0] * numbers[2]
    index = 0
    max = -2147483647
    start_i = 0
    start_j = 0
    max = NMK(index, start_i, start_j, numbers[0], numbers[1], numbers_list, visited_list, selected_list, max, x, y)
    print(max)