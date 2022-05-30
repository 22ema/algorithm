
def triangle(count, number_list, save_list):
    save_list[0][0] = number_list[0][0]
    for i in range(1, count):
        for j in range(0, i+1):
            if j + 1 > i:
                save_list[i][j] = save_list[i-1][j-1]+ number_list[i][j]
            elif j - 1 >= 0:
                save_list[i][j] = max(save_list[i-1][j-1], save_list[i-1][j])+ number_list[i][j]
            elif j - 1 < 0:
                save_list[i][j] = save_list[i-1][j] + number_list[i][j]



if __name__ == "__main__":
    count = int(input())
    number_list = list()
    save_list = list()
    for i in range(count):
        number = list(map(int, input().split()))
        number_list.append(number)
    for i in range(count):
        save_list.append([0] * (i+1))
    triangle(count, number_list, save_list)
    print(max(save_list[count-1]))