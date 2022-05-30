
def zoo(number, number_list):
    for i in range(1, number+1):
        if i == 1:
            number_list[i][0] = 1
            number_list[i][1] = 1
            number_list[i][2] = 1
        else:
            number_list[i][0] = number_list[i-1][1] + number_list[i-1][2] + number_list[i-1][0]
            number_list[i][1] = number_list[i-1][0] + number_list[i-1][2]
            number_list[i][2] = number_list[i-1][1] + number_list[i-1][0]
        number_list[i][0] %= 9901
        number_list[i][1] %= 9901
        number_list[i][2] %= 9901

if __name__ == "__main__":
    number = int(input())
    number_list = [[0]*4 for _ in range(0, number+1)]
    zoo(number, number_list)
    print(sum(number_list[number])%9901)