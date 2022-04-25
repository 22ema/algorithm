def calc_calender(M, N, x, y):
    xx = 1
    yy = 1
    count = 1
    while True:
        if x == xx and y == yy:
            break
        if M == xx and N == yy:
            return -1
        xx += 1
        yy += 1
        if xx == M +1:
            xx = 1
        if yy == N +1:
            yy = 1
        count += 1
    return count

if __name__ == "__main__":
    count_num = int(input())
    number_list = list()
    for i in range(0, count_num):
        number_list.append(list(map(int, input().split())))
    for i in number_list:
        result = calc_calender(i[0], i[1], i[2], i[3])
        print(result)