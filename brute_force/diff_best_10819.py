
def diff_best(index, number, number_list, visited_list, selected_list, maximum):
    if index == number:
        sum = 0
        for i in range(0, index-1):
            sum += abs(selected_list[i]-selected_list[i+1])
        if maximum < sum:
            maximum = sum
        return maximum
    for i in range(0, number):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        selected_list[index] = number_list[i]
        maximum = diff_best(index+1, number, number_list, visited_list, selected_list, maximum)
        visited_list[i] = False
    return maximum

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    number_list = sorted(number_list)
    visited_list = [False] * number
    index =0
    maximum = 0
    selected_list = [0] * number
    maximum = diff_best(index, number, number_list, visited_list, selected_list, maximum)
    print(maximum)