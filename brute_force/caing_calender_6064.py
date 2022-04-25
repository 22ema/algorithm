
def calc_calender(M, N, x, y):
    k = x
    z = M
    while True:
        if k%N == y:
            break
        if z%N == 0:
            return -1
        k+=M
        z+=M
    return k+1

if __name__ == "__main__":
    count_num = int(input())
    number_list = list()
    for i in range(0, count_num):
        number_list.append(list(map(int, input().split())))
    for i in number_list:
        result = calc_calender(i[0], i[1], i[2]-1, i[3]-1)
        print(result)