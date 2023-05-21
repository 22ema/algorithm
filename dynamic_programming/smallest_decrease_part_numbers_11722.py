
'''
수열 문제는 dp로 풀자
6
10 30 10 20 20 10

1  1  2  2  2  3 
10 
'''


def select_longest_number_list(number, number_list):
    result_list = [0] * number ## save length
    result_list[0] = 1
    for i in range(1, number):
        result_list[i] = 1
        for j in range(0, i):
            if number_list[i] < number_list[j] and result_list[i] < result_list[j] + 1:
                result_list[i] = result_list[j] + 1
    return max(result_list)

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    answer = select_longest_number_list(number, number_list)
    print(answer)