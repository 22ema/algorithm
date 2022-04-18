def dfs(pair_list, visited_list, count, pair_number):
    visited_list[count] = True
    for i in range(0, pair_number):
        if pair_list[i][0] == count+1 and not visited_list[pair_list[i][1]-1]:
            dfs(pair_list, visited_list, pair_list[i][1]-1, pair_number)
        if pair_list[i][1] == count+1 and not visited_list[pair_list[i][0]-1]:
            dfs(pair_list, visited_list, pair_list[i][0]-1, pair_number)


if __name__ == "__main__":
    computer_number = int(input())
    pair_number = int(input())
    pair_list = list()
    visited_list = [False]*computer_number
    count = 0
    for i in range(0, pair_number):
        pairs = list(map(int, input().split()))
        pair_list.append(pairs)
    while True:
        if not visited_list[count]:
            dfs(pair_list, visited_list, count, pair_number)
            break
    counting = 0
    for i in range(0, computer_number):
        if i!=0 and visited_list[i] == True:
            counting+=1
        else:
            pass

    print(counting)