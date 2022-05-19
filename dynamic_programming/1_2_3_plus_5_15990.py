
def plus(number, counting_list, mod):
    counting_list[1] = [0,1,0,0]
    counting_list[2] = [0, 0, 1, 0]
    counting_list[3] = [0, 1, 1, 1]
    for i in range(4, number+1):
        counting_list[i][1] = counting_list[i - 1][2] + counting_list[i - 1][3]
        counting_list[i][2] = counting_list[i - 2][1] + counting_list[i - 2][3]
        counting_list[i][3] = counting_list[i - 3][1] + counting_list[i - 3][2]
        counting_list[i][1] %= mod
        counting_list[i][2] %= mod
        counting_list[i][3] %= mod
    # for i in range(1, limit + 1):
    #     if i - 1 >= 0:
    #         d[i][1] = d[i - 1][2] + d[i - 1][3]
    #         if i == 1:
    #             d[i][1] = 1
    #     if i - 2 >= 0:
    #         d[i][2] = d[i - 2][1] + d[i - 2][3]
    #         if i == 2:
    #             d[i][2] = 1
    #     if i - 3 >= 0:
    #         d[i][3] = d[i - 3][1] + d[i - 3][2]
    #         if i == 3:
    #             d[i][3] = 1
    #     d[i][1] %= mod
    #     d[i][2] %= mod
    #     d[i][3] %= mod

if __name__ == "__main__":
    count = int(input())
    counting_list = [[0] * 4 for _ in range(100000 + 1)]
    plus(100000, counting_list, 1000000009)
    for i in range(count):
        number = int(input())
        print(sum(counting_list[number])%1000000009)