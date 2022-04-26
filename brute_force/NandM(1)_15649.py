
def choose_number(index, n, m, visited_list, number):
    if index == m:
        for i in number:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        if visited_list[i-1] == False:
            visited_list[i-1] = True
            number[index] = i
            choose_number(index+1, n, m, visited_list, number)
            visited_list[i-1] = False
        else:
            pass



if __name__=="__main__":
    count = 0
    index = 0
    number_list = list(map(int, input().split()))
    numbers = list(i for i in range(1,number_list[0]+1))
    number = [0] * number_list[1]
    visited_list = [False] * number_list[0]
    choose_number(index, number_list[0], number_list[1], visited_list, number)
