
def solution(index, N, M, save_list):
    if index == M:
        for i in save_list:
            print(i, end= " ")
        print()
        return
    for i in range(1, N+1):
        save_list[index] = i
        solution(index+1, N, M, save_list)


if __name__=="__main__":
    number_list = list(map(int, input().split()))
    index = 0
    save_list = [0] * number_list[1]
    solution(index, number_list[0], number_list[1], save_list)
