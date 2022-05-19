
MOD = 1000000000
def easy_stair(number, number_list):
    for i in range(1, number+1):
        if i == 1:
            for j in range(1, 10):
                number_list[i][j] = 1
        else:
            for j in range(0, 10):
                if j+1 >=10:
                    number_list[i][j] = number_list[i - 1][j - 1]
                elif j == 0:
                    number_list[i][j] = number_list[i - 1][j + 1]
                else:
                    number_list[i][j] = number_list[i-1][j-1] + number_list[i-1][j+1]
                number_list[i][j] %= MOD

if __name__ == "__main__":
    number = int(input())
    number_list = [[0]*10 for _ in range(number+1)]
    easy_stair(number, number_list)
    print(sum(number_list[number])%MOD)
