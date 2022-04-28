
def solution(index, start,  N, M, numbers, save_list):
    if index == M:
        for i in save_list:
            print(i, end=" ")
        print()
        return
    for i in range(start, N):
        n = numbers[i]
        save_list[index] = n
        solution(index+1, i, N, M, numbers, save_list)





if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    numbers = sorted(list(map(int, input().split())))
    index = 0
    start = 0
    save_list = [0] * number_list[1]
    visited_list = [False] * number_list[0]
    solution(index, start, number_list[0], number_list[1], numbers, save_list)