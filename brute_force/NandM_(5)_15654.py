
def solution(index, N, M, numbers, save_list, visited_list):
    if index == M:
        for i in save_list:
            print(i, end=" ")
        print()
        return
    for i in range(0, N):
        if visited_list[i] == False:
            n = numbers[i]
            visited_list[i] = True
            save_list[index] = n
            solution(index+1, N, M, numbers, save_list, visited_list)
            visited_list[i] = False




if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    numbers = sorted(list(map(int, input().split())))
    index = 0
    save_list = [0] * number_list[1]
    visited_list = [False] * number_list[0]
    solution(index, number_list[0], number_list[1], numbers, save_list, visited_list)