
def dfs(V, number_list, visited_list, save_list):
    visited_list[V] = True
    save_list.append(V+1)
    for i in range(0, len(number_list[V])):
        if visited_list[number_list[V][i]] == True:
            continue
        else:
            dfs(number_list[V][i], number_list, visited_list, save_list)

def bfs(V, number_list, visited_list, save_list):
    queue = list()
    queue.append(V)
    while len(queue) != 0:
        index = queue.pop(0)
        if visited_list[index] == False:
            visited_list[index] = True
            save_list.append(index+1)
            for i in range(0, len(number_list[index])):
                if visited_list[number_list[index][i]] == False:
                    queue.append(number_list[index][i])

if __name__ == "__main__":
    N, M, V = list(map(int, input().split()))
    number_list = [[] for _ in range(N)]
    visited_list = [False] * N
    dfs_save_list = list()
    for i in range(0, M):
        a, b = list(map(int, input().split()))
        number_list[a-1].append(b-1)
        number_list[b-1].append(a-1)
    for i in range(0, len(number_list)):
        number_list[i] = sorted(number_list[i])
    dfs(V-1, number_list, visited_list, dfs_save_list)
    for i in dfs_save_list:
        print(i, end=' ')
    print()
    visited_list = [False] * N
    bfs_save_list = list()
    bfs(V-1, number_list, visited_list, bfs_save_list)
    for i in bfs_save_list:
        print(i, end=' ')