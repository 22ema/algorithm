import copy
def very_long(number, number_list, save_list, index_list):
    for i in range(1, number+1):
        save_list[i] = 1
        for j in range(1, i):
            if number_list[i-1] > number_list[j-1] and save_list[i] < (save_list[j]+1):
                save_list[i] = save_list[j] + 1
                index_list[i] = copy.deepcopy(index_list[j])
        index_list[i].append(number_list[i-1])

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    save_list = [0] * (number+1)
    index_list = [list() for _ in range(number+1)]
    very_long(number, number_list, save_list, index_list)
    print(max(save_list))
    temp = len(index_list[1])
    best_index = 1
    for i in range(2, number+1):
        if len(index_list[i]) > temp:
            temp = len(index_list[i])
            best_index = i
    for i in index_list[best_index]:
        print(i, end=" ")
