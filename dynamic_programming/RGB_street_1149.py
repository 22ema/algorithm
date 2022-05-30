
def RGB_street(number, number_list, save_list):
    for i in range(0, number):
        for j in range(0, 3):
            if i == 0:
                save_list[i][j] = number_list[i][j]
            else:
                if j == 0:
                    save_list[i][j] = min(save_list[i-1][1], save_list[i-1][2]) + number_list[i][j]
                elif j == 1:
                    save_list[i][j] = min(save_list[i-1][0], save_list[i-1][2]) + number_list[i][j]
                elif j == 2:
                    save_list[i][j] = min(save_list[i-1][0], save_list[i-1][1]) + number_list[i][j]


if __name__ == "__main__":
    number = int(input())
    number_list = list(list(map(int, input().split())) for _ in range(number))
    save_list = [[0] * 3 for _ in range(0, number)]
    RGB_street(number, number_list, save_list)
    print(min(save_list[number-1]))