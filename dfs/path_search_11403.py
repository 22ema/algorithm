def dfs(route_list, visited_list, count, number, result_list):
    for i in range(0, number):
        if route_list[count][i] == 1 and visited_list[i] == False:
            visited_list[i] = True
            dfs(route_list, visited_list, i, number, result_list)
            result_list[i] = 1

if __name__ == "__main__":
    count = 0
    number = int(input())
    graph_list = list()
    # route_list = list()
    result_list = [ [0]*number for _ in range(0, number)]
    for i in range(0, number):
        graph = list(map(int, input().split()))
        graph_list.append(graph)
    # for i in range(0, number):
    #     for j in range(0, number):
    #         if graph_list[i][j] == 1:
    #             route_list.append([i, j])
while count != number:
    visited_list = [False]*number
    dfs(graph_list, visited_list, count, number, result_list[count])
    count+=1
for i in result_list:
    for j in i:
        print(j, end=" ")
    print()