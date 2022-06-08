import math
def solution(progresses, speeds):
    save_list = [0] * len(progresses)
    for i in range(0, len(progresses)):
        number = math.ceil((100 - progresses[i])/speeds[i])
        save_list[i] = number
    count = 1
    temp = save_list[0]
    ans = list()
    print(save_list)
    for i in range(0, len(save_list)-1):
        if temp >= save_list[i+1]:
            count += 1
            if i == len(save_list)-2:
                ans.append(count)
        else:
            temp = save_list[i+1]
            ans.append(count)
            count = 1
            if i == len(save_list)-2:
                ans.append(count)
    return ans




if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = 	[1, 1, 1, 1, 1, 1]
    ans = solution(progresses, speeds)
    print(ans)