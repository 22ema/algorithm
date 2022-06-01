
def dfs(index, number_list, visited_list):
    visited_list[index] = True
    for i in range(0, len(number_list[index])):
        if visited_list[number_list[index][i]] == False:
            dfs(number_list[index][i], number_list, visited_list)


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    number_list = [[] for _ in range(N)]
    visited_list = [False] * N
    count = 0
    for i in range(0, M):
        a, b = list(map(int, input().split()))
        number_list[a-1].append(b-1)
        number_list[b-1].append(a-1)
    for i in range(0, N):
        if visited_list[i] == True:
            continue
        count+=1
        dfs(i, number_list, visited_list)
    print(count)
