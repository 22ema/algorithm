

def pin_num(number, number_list):
    for i in range(1, number+1):
        if i == 1:
            number_list[i][1] = 1
        elif i == 2 :
            number_list[i][0] = 1
        elif i == 3:
            number_list[i][0] = 1
            number_list[i][1] = 1
        else:
            number_list[i][1] = number_list[i-1][0]
            number_list[i][0] = number_list[i-1][1] + number_list[i-1][0]



if __name__ == "__main__":
    number = int(input())
    number_list = [[0] * 2 for _ in range(number+1)]
    pin_num(number, number_list)
    print(sum(number_list[number]))