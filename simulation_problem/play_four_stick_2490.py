
def calc_stick(count):
    if count == 0:
        return 'E'
    elif count == 1:
        return 'A'
    elif count == 2:
        return 'B'
    elif count == 3:
        return 'C'
    elif count == 4:
        return 'D'

if __name__ == '__main__':
    sticks_list = list()
    result_list = list()
    for i in range(0,3):
        sticks_list.append(map(int, input().split()))
    for i in sticks_list:
        count=0
        for j in i:
            if j == 0:
                count += 1
        result_list.append(calc_stick(count))
    for i in result_list:
        print(i)