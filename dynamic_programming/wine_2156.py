
def wine(count, number_list, save_list):
    save_list[1][0] = 0
    save_list[1][1] = number_list[0]
    save_list[1][2] = number_list[0]
    for i in range(2, count+1):
        save_list[i][0] = max(save_list[i-1])
        save_list[i][1] = max(save_list[i-2]) + number_list[i-1]
        save_list[i][2] = save_list[i-1][1] + number_list[i-1]



if __name__ == "__main__":
    count = int(input())
    number_list = list()
    for i in range(count):
        number = int(input())
        number_list.append(number)
    save_list = [[0] * 3 for _ in range(0,count+1)]
    wine(count, number_list, save_list)
    print(max(save_list[count]))