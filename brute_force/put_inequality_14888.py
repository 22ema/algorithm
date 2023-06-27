'''
곱셈이랑 나눗셈을 먼저 배치시키고 처리하는게 좋아보임
'''


inequal = ['+', '-', '*', '/']

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def check_inequal(inequal_list, number_list):
    inequal_list_len = len(inequal_list)
    now = 0
    for i in range(0, inequal_list_len):
        if i == 0:
            now = number_list[i]
        if '/' == inequal[inequal_list[i]]:
            now = int(now / number_list[i+1])
        elif '*' == inequal[inequal_list[i]]:
            now = now * number_list[i+1]
        elif '-' == inequal[inequal_list[i]]:
            now = now - number_list[i+1]
        elif '+' == inequal[inequal_list[i]]:
            now = now + number_list[i+1]
    return now

if __name__ == "__main__":
    N = int(input())
    min_num = 1000000000
    max_num = -1000000000
    number_list = list(map(int, input().split(' ')))
    inequal_number_list = list(map(int, input().split(' ')))
    total_inequal_list = list()
    for i in range(3, -1, -1):
        for j in range(0, inequal_number_list[i]):
            total_inequal_list.append(i)
    total_inequal_list.sort()
    while True:
        now = check_inequal(total_inequal_list, number_list)
        # print("now:\t", now)
        if max_num < now:
            max_num = now
        if min_num > now:
            min_num = now
        if not next_permutation(total_inequal_list):
            break
    print(max_num)
    print(min_num)
    
