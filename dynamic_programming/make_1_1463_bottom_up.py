
def make_1(number, number_list):
    number_list[1] = 0
    for i in range(2, number+1):
        number_list[i] = number_list[i-1] +1
        if i % 2 == 0 and number_list[i] > number_list[i//2]+1:
            number_list[i] = number_list[i//2] + 1
        if i % 3 == 0 and number_list[i] > number_list[i//3]+1:
            number_list[i] = number_list[i//3] + 1
    print(number_list[number])





if __name__ == "__main__":
    number = int(input())
    number_list = [0] * (number+1)
    make_1(number, number_list)