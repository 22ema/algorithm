
def bit_mask(N, M, number_list, ans):
    flag = 0
    for i in range(1, 1<<N):
        sum = 0
        for k in range(N):
            if i&(1<<k):
                sum += number_list[k]
                flag = 1
        if sum == M and flag ==1:
            ans += 1
    return ans

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    ans = 0
    ans = bit_mask(input_list[0], input_list[1], number_list, ans)
    print(ans)