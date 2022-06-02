import sys
sys.setrecursionlimit(1000000)
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
def dfs(n, m, apart_list, visited_list, apart_count, count):
    visited_list[n][m] = count
    for i in range(0, 4):
        xx = n + x[i]
        yy = m + y[i]
        if xx < 0 or yy < 0 or yy >= len(apart_list) or xx >= len(apart_list):
            continue
        if visited_list[xx][yy] == 0 and apart_list[xx][yy] == '1':
            visited_list[xx][yy] = count
            apart_count += 1
            apart_count = dfs(xx, yy, apart_list, visited_list, apart_count, count)
    return apart_count



if __name__ == "__main__":
    number = int(input())
    apart_list = list()

    for i in range(0,number):
        apart = list(input())
        apart_list.append(apart)
    visited_list = [[0]*number for _ in range(number)]
    count = 1
    apart_counts = list()
    for i in range(0, number):
        for j in range(0, number):
            if visited_list[i][j] == 0 and apart_list[i][j]=='1':
                apart_count = 1
                apart_count = dfs(i, j, apart_list, visited_list, apart_count, count)
                if apart_count != 0:
                    count += 1
                    apart_counts.append(apart_count)
    print(count-1)
    apart_counts = sorted(apart_counts)
    for i in apart_counts:
        print(i)
