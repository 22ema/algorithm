
def inequality_sign(index, signs, min, max, select_list, visited_list):
    if index == len(select_list):
        temp = list()
        for i in range(0, len(select_list)-1):
            if signs[i] == '<':
                if select_list[i] < select_list[i+1]:
                    temp.append(select_list[i])
                    if i == len(select_list)-2:
                        temp.append(select_list[i+1])
                else:
                    return min, max
            elif signs[i] == '>':
                if select_list[i] > select_list[i+1]:
                    temp.append(select_list[i])
                    if i == len(select_list)-2:
                        temp.append(select_list[i+1])
                else :
                    return min, max
        for i in range(0, len(temp)):
            if min[i] < temp[i]:
                break
            elif min[i] > temp[i]:
                min = temp
                break
            else:
                pass
        for i in range(0, len(temp)):
            if max[i] > temp[i]:
                break
            elif max[i] < temp[i]:
                max = temp
                break
            else:
                pass
        return min, max



    for i in range(0, 10):
        if visited_list[i] == True:
            continue
        select_list[index] = i
        visited_list[i] = True
        min, max = inequality_sign(index+1, signs, min, max, select_list, visited_list)
        visited_list[i] = False
    return min, max

if __name__ == "__main__":
    number = int(input())
    signs = list(input().split())
    min = [9] * (number+1)
    max = [0] * (number+1)
    select_list = [0] * (number+1)
    index = 0
    visited_list = [False] * 10
    min, max = inequality_sign(index, signs, min, max, select_list, visited_list)
    for i in max:
        print(i, end="")
    print()
    for i in min:
        print(i, end="")