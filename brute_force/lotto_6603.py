
def lotto(index, start, number_count, number_list, visited_list, seleted_list):
    if index == 6:
        for i in range(index):
            print(selected_list[i], end=" ")
        print("")
        return 0


    for i in range(start,number_count):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        selected_list[index] = number_list[i]
        lotto(index+1, i , number_count, number_list, visited_list, seleted_list)
        visited_list[i] = False


if __name__ == "__main__":
    while True:
        number_list = list(map(int, input().split()))
        if number_list[0] == 0:
            break
        number_count = number_list[0]
        index = 0
        start = 0
        visited_list = [False] * number_count
        selected_list = [0] * 6
        lotto(index, start, number_count, number_list[1:], visited_list, selected_list)
        print("")
