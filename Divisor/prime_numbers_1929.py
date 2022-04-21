if __name__ == "__main__":
    number_list =list(map(int, input().split()))
    result_list = list()

    result = 0
    for i in range(0, number_list[1]+1):
        result_list.append(i)
    for i in range(2, int(number_list[1]**(1/2))+1):
        number = 2
        while True:
            result = number * i
            number += 1
            if result < number_list[1]+1:
                result_list[result] = 0
            else:
                break
    for i in range(number_list[0], number_list[1]+1):
        if result_list[i]!=0 and result_list[i]!=1:
            print(result_list[i])