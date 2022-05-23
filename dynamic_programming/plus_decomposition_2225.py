mod = 1000000000
def plus_decom(N, M, number_list):
    count = 0
    for i in range(1, M+1):
        for j in range(0, N+1):
            for l in range(0, j+1):
                number_list[i][j] += number_list[i-1][j-l]
            number_list[i][j] %= mod
    return count




if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    save_list = [0] * numbers[1]
    number_list = [[0] * (numbers[0]+1) for i in range(numbers[1]+1)]
    number_list[0][0] = 1
    count = plus_decom(numbers[0], numbers[1], number_list)
    print(number_list[numbers[1]][numbers[0]])
