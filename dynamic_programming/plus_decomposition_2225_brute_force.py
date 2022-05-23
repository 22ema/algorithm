
def plus_decom(index, N, M, visited_list, save_list, count):
    if index == M:
        sum_num = 0
        for i in save_list:
            sum_num += i
        if sum_num == N:
            count += 1
        return count
    for i in range(0,N+1):
        # if visited_list[i] == True:
        #     continue
        # visited_list[i] = True
        save_list[index] = i
        count = plus_decom(index+1, N, M, visited_list, save_list, count)
        # visited_list[i] = False
    return count



if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    index = 0
    visited_list = [0] * numbers[0]
    save_list = [0] * numbers[1]
    count = 0
    count = plus_decom(index, numbers[0], numbers[1], visited_list, save_list, count)
    print(count)