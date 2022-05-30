

def sum(number, number_list):
    for i in range(1, number+1):
        if i == 1:
            number_list[i] = 1
        elif i == 2:
            number_list[i] = 2
        elif i == 3:
            number_list[i] = 4
        else:
            number_list[i] = number_list[i-3] + number_list[i-2] +number_list[i-1]
        number_list[i] %= 1000000009


if __name__=="__main__":
    count = int(input())
    number_list = [0] * (1000001)
    sum(1000000, number_list)
    for i in range(count):
        number = int(input())
        print(number_list[number])