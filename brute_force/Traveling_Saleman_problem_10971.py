
def TSP(index, number, maps, visited_list, selected_list, result):
    if index == number:
        sum = 0
        for i in range(0, index-1):
            if maps[selected_list[i]][selected_list[i+1]] == 0:
                return result
            sum += maps[selected_list[i]][selected_list[i+1]]
            if i == index-2:
                if maps[selected_list[index-1]][selected_list[0]] == 0:
                    return result
                sum += maps[selected_list[index-1]][selected_list[0]]
        if result > sum:
            result = sum
        return result

    for i in range(0, number):
        if selected_list[0]!=0:
            break
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        selected_list[index] = i
        result = TSP(index+1, number, maps, visited_list, selected_list, result)
        visited_list[i] = False
    return result


if __name__ == "__main__":
    number = int(input())
    maps = [list(map(int, input().split())) for _ in range(number)]
    visited_list = [False] * number
    selected_list = [0] * number
    index = 0
    result = 2147483647
    result = TSP(index, number, maps, visited_list, selected_list, result)
    print(result)
