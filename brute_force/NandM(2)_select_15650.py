
def solution(index, selected, N, M, save_list):
    if selected == M:
        print(save_list)
        return
    if index > N : return
    save_list[selected] = index
    solution(index+1, selected+1, N, M, save_list)
    save_list[selected] = 0
    solution(index+1, selected, N, M, save_list)


if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    save_list = [0]*number_list[1]
    index = 1
    selected = 0
    solution(index, selected, number_list[0], number_list[1], save_list)

