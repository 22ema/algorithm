
def bit_mask(N, M, number_list):
    max = 0
    for i in range(1<<N*M):
        sum = 0
        for j in range(N):
            cur = 0
            for k in range(M):
                if i&(1<<k+(j*M)) == 0:
                    cur = cur * 10 +int(number_list[j][k])
                else:
                    sum+= cur
                    cur =0
            sum += cur
        for k in range(M):
            cur = 0
            for j in range(N):
                if i&(1<<k+(j*M)):
                    cur = cur * 10 + int(number_list[j][k])
                else:
                    sum += cur
                    cur = 0
            sum += cur
        if max < sum:
            max = sum
    return max


if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    number_list = [list(input()) for _ in range(input_list[0])]
    max = bit_mask(input_list[0], input_list[1], number_list)
    print(max)
