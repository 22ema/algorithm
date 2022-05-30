
def up_hill(number, number_list):
    for i in range(0, number+1):
        number_list[1][i] = 1
        for j in range(0, i):
            number_list[i][j] += number_list[i-1][k]

if __name__ == "__main__":
    number = int(input())
    number_list = [[0] * 10 for _ in range(0, number+1)]
    up_hill(number, number_list)