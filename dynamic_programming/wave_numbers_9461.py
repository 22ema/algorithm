
def wave_numbers(number):
    number_list = [0] * 100
    number_list[0] = 1
    number_list[1] = 1
    number_list[2] = 1
    number_list[3] = 2
    number_list[4] = 2
    for i in range(5, number):
        number_list[i] = number_list[i-1] + number_list[i-5]
    return number_list[number-1]

if __name__ == "__main__":
    testcase = int(input())
    for i in range(0, testcase):
        number = int(input())
        answer = wave_numbers(number)
        print(answer)
