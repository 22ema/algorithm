def bfs(shark_x, shark_y, fish_list, min_dist, umber, fish_size):
    visited_list = [[False]*number for _ in range(number)]
    new_visit = [[False]*number]*number
    visited_list[shark_x][shark_y] = True
    q = list()
    q.append((shark_x, shark_y, 0))
    dist_list = list()

    while len(q):
        x, y, dist = q.pop(0)
        for i in range(0,4):
            xx = x_list[i] + x
            yy = y_list[i] + y
            if 0<= xx < number and 0<= yy < number and visited_list[xx][yy] == False:
                if fish_list[xx][yy] <= fish_size:
                    visited_list[xx][yy] = True
                    if 0 < fish_list[xx][yy] < fish_size:
                        min_dist = dist
                        dist_list.append((dist+1, xx, yy))
                    if dist+1 <= min_dist:
                        q.append((xx, yy, dist+1))
    if len(dist_list):
        dist_list.sort()
        return dist_list[0]
    else:
        return False


if __name__ == "__main__":
    number = int(input())
    fish_list = list()
    x_list = [0, 0, 1, -1]
    y_list = [1, -1, 0, 0]
    min_dist = 1e9
    dist = 0
    fish_number = 0
    eat_count = 0
    fish_size = 2
    shark_x = 0
    shark_y = 0
    time = 0
    for i in range(0, number):
        fish_list.append(list(map(int,input().split())))
    for i in range(0, number):
        for j in range(0, number):
            if 0 < fish_list[i][j] and fish_list[i][j] < 7:
                fish_number += 1
            elif fish_list[i][j] == 9:
                shark_x = i
                shark_y = j
                fish_list[i][j] = 0
    while fish_number:
        result = bfs(shark_x, shark_y, fish_list, min_dist, number, fish_size)
        if not result:
            break
        shark_x, shark_y = result[1], result[2]
        dist = result[0]
        eat_count += 1
        fish_number -= 1
        if fish_size == eat_count:
            fish_size += 1
            eat_count = 0
        fish_list[shark_x][shark_y] = 0
        time+=dist
    print(time)

