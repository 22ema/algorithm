
def perm(index, number, select_list, visited_list):
    if index == number:
        for i in select_list:
            print(i, end=" ")
        print()
        return 0
    for i in range(0, number):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        select_list[index] = i+1
        perm(index+1, number, select_list, visited_list)
        visited_list[i] = False
if __name__=="__main__":
    number = int(input())
    select_list = [0] * number
    visited_list = [False] * number
    perm(0, number, select_list, visited_list)
