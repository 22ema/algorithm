
in_eq_list = ['+', '-', '*', '/']



def check_inequal(inequal_list, number_list):
    inequal_list_len = len(inequal_list)
    now = 0
    for i in range(0, inequal_list_len):
        if i == 0:
            now = number_list[i]
        if '/' == in_eq_list[inequal_list[i]]:
            now = int(now / number_list[i+1])
        elif '*' == in_eq_list[inequal_list[i]]:
            now = now * number_list[i+1]
        elif '-' == in_eq_list[inequal_list[i]]:
            now = now - number_list[i+1]
        elif '+' == in_eq_list[inequal_list[i]]:
            now = now + number_list[i+1]
    return now
    

def solve(numbers, in_eq, visited_eq_list, choose_list, prev, max, min):
    if len(choose_list) == len(numbers)-1:
        ans = check_inequal(choose_list, numbers)
        if max < ans:
            max = ans
        if min > ans:
            min = ans
        return max, min
    for i, value in enumerate(in_eq):
        if visited_eq_list[i] is True:
            continue
        if prev[in_eq[i]] == True:
            continue
        else:
            prev = [False] * 4
        choose_list.append(in_eq[i])
        visited_eq_list[i] = True
        max, min = solve(numbers, in_eq, visited_eq_list, choose_list, prev, max, min)
        prev[in_eq[i]] = True
        visited_eq_list[i] = False
        choose_list.pop()
    return max, min



if __name__ == "__main__":
    MAX = -100000000
    MIN = 1000000000
    N = int(input())
    numbers = list(map(int, input().split(' ')))
    in_eq = list(map(int, input().split(' ')))
    total_eq_list = list()
    n = 0
    choose_list = list()
    for i in range(0, 4):
        if in_eq[i] >= len(numbers)-1:
            in_eq[i] = len(numbers)-1
    for i in range(0, 4):
        for j in range(0, in_eq[i]):
            total_eq_list.append(i)
    visited_eq_list = [False] * len(total_eq_list)
    prev = [False] * 4
    max, min = solve(numbers, total_eq_list, visited_eq_list, choose_list, prev, MAX, MIN)
    print(max)
    print(min)


# def calc(a, index, cur, plus, minus, mul, div):
#     if index == len(a):
#         return (cur, cur)
#     res = []
#     if plus > 0:
#         res.append(calc(a,index+1,cur+a[index],plus-1,minus,mul,div))
#     if minus > 0:
#         res.append(calc(a,index+1,cur-a[index],plus,minus-1,mul,div))
#     if mul > 0:
#         res.append(calc(a,index+1,cur*a[index],plus,minus,mul-1,div))
#     if div > 0:
#         if cur >= 0:
#             res.append(calc(a,index+1,cur//a[index],plus,minus,mul,div-1))
#         else:
#             res.append(calc(a,index+1,-(-cur//a[index]),plus,minus,mul,div-1))
#     ans = (
#         max([t[0] for t in res]),
#         min([t[1] for t in res])
#     )

#     return ans

# n = int(input())
# a = list(map(int,input().split()))
# plus,minus,mul,div = map(int,input().split())
# ans = calc(a, 1, a[0], plus, minus, mul, div)
# print(ans[0])
# print(ans[1])