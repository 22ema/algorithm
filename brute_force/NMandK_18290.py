def solution(index, N, M, z, mapping_list, sum_number, result, index_list, visited_list, dx, dy):
    if index == z:
        if sum_number > result:
            result = sum_number
        return result
    for i in range(0, M):
        for j in range(0, N):
            if visited_list[i][j] == True:
                break
            ok = True
            for k in range(0, 4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx and nx<M and 0<=ny and ny < N:
                    if visited_list[nx][ny] :
                        ok = False

            if ok == True:
                visited_list[i][j] = True
                result = solution(index+1, N, M, z, mapping_list, sum_number+mapping_list[i][j],
                                  result, index_list, visited_list, dx, dy)
                visited_list[i][j] = False
    return result


if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    mapping_list = [list(map(int, input().split())) for _ in range(0,number_list[1])]
    index = 0
    sum_number = 0
    result = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited_list = [[False]*number_list[0] for _ in range(0, number_list[1])]
    index_list = list()
    result = solution(index, number_list[0], number_list[1], number_list[2],
                      mapping_list, sum_number, result, index_list, visited_list, dx, dy)
    print(result)