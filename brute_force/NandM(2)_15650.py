
def solution(index, start, N, M, visited_list, number_list, real_visited_list):
    if index == M:
        for i in range(0, M):
            print(number_list[i], end=" ")
        print()
        return
    for i in range(start, N):
        if visited_list[i] == False:
            visited_list[i] = True
            number_list[index] = i+1
            solution(index+1, i+1, N, M, visited_list, number_list, real_visited_list)
            visited_list[i] = False
        else:
            pass




if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    index = 0
    start = 0
    numbers_list = [0] * number_list[1]
    visited_list = [False] * number_list[0]
    real_visited_list = [False] * number_list[0]
    solution(index, start, number_list[0], number_list[1], visited_list, numbers_list, real_visited_list)