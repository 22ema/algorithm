x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
start = [0, 0]

def dfs(n,m,map_list, visited_list,k, result):
    visited_list[n][m] = True
    if n==len(map_list)-1 and m == len(map_list[0])-1:
        return
    for i in range(0, 4):
        xx = x[i] + n
        yy = y[i] + m
        if xx >= len(map_list) or yy >= len(map_list[0]) or yy < 0 or xx <0 or map_list[xx][yy] == '#' or visited_list[xx][yy] == True:
            continue
        if k == 0:
            return False
        dfs(xx, yy, map_list, visited_list, k-1)





def solution(grid, k):
    map_list = list()
    for i in range(0, len(grid)):
        map_list.append(list(grid[i]))
    visited_list = [[False] * len(map_list) for _ in range(0, len(map_list[0]))]
    result = 0
    dfs(start[0], start[1], map_list, visited_list, k, result)



if __name__ == "__main__":
    grid = ["..FF", "###F", "###."]
    k = 4
    solution(grid, k)