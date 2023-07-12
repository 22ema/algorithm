
def make_total_list(numbers, total_list, finish_list, visited_list, n):
    for i in range(n, len(numbers)):
        if visited_list[i] == True:
            continue
        total_list.append(numbers[i])
        finish_list.append(sum(total_list))
        visited_list[i] = True
        make_total_list(numbers, total_list, finish_list, visited_list, i+1)
        visited_list[i] = False
        total_list.pop()

if __name__ == "__main__":
    s = int(input())
    n = 0
    numbers = list(map(int, input().split(' ')))
    total_list = list()
    finish_list = list()
    visited_list = [False] * s
    make_total_list(numbers, total_list, finish_list, visited_list, n)
    finish_list = list(set(finish_list))
    finish_list.sort()
    i = 0
    while True:
        j = i + 1
        if finish_list[i] != j:
            print(j)
            break
        elif i == len(finish_list)-1:
            print(j+1)
            break
        i+=1


