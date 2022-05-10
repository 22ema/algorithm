
def do_consulting(start, count, numbers_list, visited_list, max, sum):
    if start == len(numbers_list):
        if max < sum:
            max = sum
        return max
    elif start > len(numbers_list):
        return max
    if max < sum:
        max = sum
    for i in range(start, count):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        max = do_consulting(i+numbers_list[i][0], count, numbers_list, visited_list, max, sum+numbers_list[i][1])
        visited_list[i] = False
    return max
if __name__ == "__main__":
    count = int(input())
    numbers_list = list()
    start = 0
    sum = 0
    max = 0
    visited_list = [False] * count
    for i in range(count):
        numbers_list.append(list(map(int, input().split())))
    max = do_consulting(start, count, numbers_list, visited_list, max, sum)
    print(max)