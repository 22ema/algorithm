

def solution(priorities, location):
    queue = list()
    check_location = location
    count = 0
    while True:
        location -=1
        number = priorities.pop(0)
        flag = 1
        for i in priorities:
            if i > number:
                flag = 0
                priorities.append(number)
                if location == -1:
                    location = len(priorities)-1
                break
        if flag == 1:
            count+=1
            if location == -1:
                break
    return count




if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    answer = solution(priorities, location)
    print(answer)