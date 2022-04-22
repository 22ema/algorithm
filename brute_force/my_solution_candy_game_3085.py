import copy

def dfs(temp_arr, visited_arr, i, j, x, y, result):
    visited_arr[i][j] = True
    for count in range(0, 2):
        xx = i+x[count]
        yy = j+y[count]
        if 0 <= xx < len(temp_arr) and 0 <= yy < len(temp_arr) :
            if not visited_arr[xx][yy] and temp_arr[i][j] == temp_arr[xx][yy]:
                result += 1
                result = dfs(temp_arr, visited_arr, xx, yy, x, y,result)

        else:
            pass
    return result

def dfs_2(temp_arr, visited_arr, i, j, x, y, result):
    visited_arr[i][j] = True
    for count in range(2, 4):
        xx = i+x[count]
        yy = j+y[count]
        if 0 <= xx < len(temp_arr) and 0 <= yy < len(temp_arr) :
            if not visited_arr[xx][yy] and temp_arr[i][j] == temp_arr[xx][yy]:
                result += 1
                result = dfs_2(temp_arr, visited_arr, xx, yy, x, y,result)

        else:
            pass
    return result


def search_max_candy(arr, x, y):
    max = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            for count in range(0, 2):
                if 0 <= i+x_b[count] < len(arr) and 0 <= j+y_b[count]  < len(arr):
                    temp = arr[i][j]
                    arr[i][j] = arr[i+x_b[count]][j+y_b[count]]
                    arr[i+x_b[count]][j+y_b[count]] = temp
                    for k in range(0, len(arr)):
                        for l in range(0, len(arr)):
                            visited_arr = [[False] * len(arr) for _ in range(0, len(arr))]
                            if visited_arr[k][l] == False:
                                result = 1
                                result = dfs(arr, visited_arr, k, l, x, y, result)
                                result_2 = 1
                                result_2 = dfs_2(arr, visited_arr, k, l, x, y, result_2)
                            else:
                                pass
                            if result > max:
                                max = result
                            if result_2 > max:
                                max = result_2
                    temp = arr[i+x_b[count]][j+y_b[count]]
                    arr[i+x_b[count]][j+y_b[count]] = arr[i][j]
                    arr[i][j] = temp

                else:
                    break
    return max


if __name__=="__main__":
    number = int(input())
    arr = [list(input()) for _ in range(number)]
    x= [1, -1, 0, 0]
    y =[0, 0, 1, -1]
    x_b = [1, 0]
    y_b= [0, 1]
    result = search_max_candy(arr, x, y)
    print(result)