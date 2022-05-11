
def start_link(index, human_number, number_list, first, second):
    if index == human_number:
        if len(first) != human_number//2:
            return -1
        if len(second) != human_number//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(human_number//2):
            for j in range(human_number//2):
                if i == j:
                    continue
                t1 += number_list[first[i]][first[j]]
                t2 += number_list[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    ans = -1
    t1 = start_link(index+1, human_number, number_list, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = start_link(index+1, human_number, number_list, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans



if __name__ == "__main__":
    human_number = int(input())
    number_list = [list(map(int, input().split())) for i in range(human_number)]
    visited_list = [False] * human_number
    start_team = list()
    link_team = list()
    result = start_link(0, human_number, number_list, start_team, link_team)
    print(result)