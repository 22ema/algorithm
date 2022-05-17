import sys
sys.setrecursionlimit(10000000)
def make_1(number, number_list):
    if number == 1:
        return 0
    if number_list[number] > 0:
        return number_list[number]

    number_list[number] = make_1(number - 1, number_list) + 1
    if number % 3 == 0:
        temp = make_1(number//3, number_list) + 1
        if temp < number_list[number]:
            number_list[number] = temp
    if number % 2 == 0:
        temp = make_1(number//2, number_list) + 1
        if temp < number_list[number]:
            number_list[number] = temp
    return number_list[number]





if __name__ == "__main__":
    number = int(input())
    number_list = [0] * (number+1)
    make_1(number, number_list)
    print(number_list[number])