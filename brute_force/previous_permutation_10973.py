
def prev_perm(number, number_list):
    for i in range(number-1, 0, -1):
        if number_list[i] < number_list[i-1]:
            min = i
            for j in range(i, number):
                if number_list[min] < number_list[j] and number_list[i-1] > number_list[j]:
                    min = j
            temp = number_list[min]
            number_list[min] = number_list[i-1]
            number_list[i-1] = temp
            number_list[i:] = sorted(number_list[i:], reverse=True)
            return number_list
        else:
            pass
    return -1

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    number_list = prev_perm(number, number_list)
    if number_list == -1:
        print(number_list)
    else:
        for i in number_list:
            print(i, end=" ")