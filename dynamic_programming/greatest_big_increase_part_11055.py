
## 5 3 

def part_of_number(number_list, number):
    result_list = [0] * number
    result_list[0] += number_list[0]
    for i in range(1, number):
        result_list[i] += number_list[i]
        for j in range(0, i):
            if number_list[i] > number_list[j] and result_list[i] < result_list[j] + number_list[i]:
                result_list[i] = number_list[i] + result_list[j]
    return max(result_list)


if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    answer = part_of_number(number_list, number)
    print(answer)