
# def inequality_sign(index, signs, min, max, select_list, visited_list):
#     if index == len(select_list):
#         temp = list()
#         for i in range(0, len(select_list)-1):
#             if signs[i] == '<':
#                 if select_list[i] < select_list[i+1]:
#                     temp.append(select_list[i])
#                     if i == len(select_list)-2:
#                         temp.append(select_list[i+1])
#                 else:
#                     return min, max
#             elif signs[i] == '>':
#                 if select_list[i] > select_list[i+1]:
#                     temp.append(select_list[i])
#                     if i == len(select_list)-2:
#                         temp.append(select_list[i+1])
#                 else :
#                     return min, max
#         for i in range(0, len(temp)):
#             if min[i] < temp[i]:
#                 break
#             elif min[i] > temp[i]:
#                 min = temp
#                 break
#             else:
#                 pass
#         for i in range(0, len(temp)):
#             if max[i] > temp[i]:
#                 break
#             elif max[i] < temp[i]:
#                 max = temp
#                 break
#             else:
#                 pass
#         return min, max



#     for i in range(0, 10):
#         if visited_list[i] == True:
#             continue
#         select_list[index] = i
#         visited_list[i] = True
#         min, max = inequality_sign(index+1, signs, min, max, select_list, visited_list)
#         visited_list[i] = False
#     return min, max

# if __name__ == "__main__":
#     number = int(input())
#     signs = list(input().split())
#     min = [9] * (number+1)
#     max = [0] * (number+1)
#     select_list = [0] * (number+1)
#     index = 0
#     visited_list = [False] * 10
#     min, max = inequality_sign(index, signs, min, max, select_list, visited_list)
#     for i in max:
#         print(i, end="")
#     print()
#     for i in min:
#         print(i, end="")
# '''

# [0 < 2 > ]

# [0, 1, 2]

# '''
# passes = False

# def check(sign_list, result_list):
#     for i in range(0, len(sign_list)):
#         if '<' == sign_list[i] and result_list[i] >= result_list[i+1]:
#             return False
#         elif '>' == sign_list[i] and result_list[i] <= result_list[i+1]:
#             return False
#     return True


# def choice_number(N, sign_list, number_list, visited_list, result_list, answer, flag, passes):
#     if passes == True:
#         return answer
#     finished = True 
#     for i in range(0, N+1):
#         if visited_list[i] is False:
#             finished = False
#             break
#     if finished == True:
#         result_num = int(''.join(result_list))
#         if not check(sign_list, result_list):
#             return answer
#         if flag == 'small':
#             if answer > result_num:
#                 answer = result_num
#                 passes = True
#                 return answer
#         elif flag == 'max':
#             if answer < result_num:
#                 answer = result_num
#                 passes = True
#                 return answer

#     for i in range(0, N+1):
#         if visited_list[i] == True:
#             continue
#         visited_list[i] = True;
#         result_list.append(number_list[i])
#         answer = choice_number(N, sign_list, number_list, visited_list, result_list, answer, flag, passes)
#         result_list.pop()
#         visited_list[i] = False
#     return answer

# if __name__ == "__main__":
#     N = int(input())
#     small_answer = 10000000000
#     big_answer =0
#     result_list = list()
#     sign_list = input().split(' ')
#     small_number_list = [str(i) for i in range(0, N+1)]
#     max_number_list = [str(i) for i in range(9, 9-N-1, -1)]
#     visited_list = [False] * (N+1)
#     passes = False
#     small_answer = choice_number(N, sign_list, small_number_list, visited_list, result_list, small_answer, 'small', passes)
#     visited_list = [False] * (N+1)
#     passes = False
#     big_answer = choice_number(N, sign_list, max_number_list, visited_list, result_list, big_answer, 'max', passes)
#     print(big_answer)
#     print(small_answer)

'''

'''

def check(number_list, sign_list):
    N = len(sign_list)
    for i in range(0, N):
        if sign_list[i] == "<" and number_list[i] >= number_list[i+1]:
            return False
        if sign_list[i] == ">" and number_list[i] <= number_list[i+1]:
            return False
    return True

def next_permutation(number_list):
    i = len(number_list) - 1
    while i > 0 and number_list[i-1] >= number_list[i]:
        i -= 1
    if i <= 0:
        return False
    
    j = len(number_list) - 1
    while number_list[i-1] >= number_list[j]:
        j -= 1
    number_list[i-1], number_list[j] = number_list[j], number_list[i-1]
    j = len(number_list) - 1
    while i < j:
        number_list[i], number_list[j] = number_list[j], number_list[i]
        i += 1
        j -= 1
    return True

def prev_permutation(number_list):
    i = len(number_list) - 1
    while i > 0 and number_list[i-1] <= number_list[i]:
        i -= 1
    if i <= 0:
        return False
    
    j = len(number_list) - 1
    while number_list[i-1] <= number_list[j]:
        j -= 1
    number_list[i-1], number_list[j] = number_list[j], number_list[i-1]

    j = len(number_list) - 1
    while i < j:
        number_list[i], number_list[j] = number_list[j], number_list[i]
        i += 1
        j -= 1
    return True

        


def solve(small_number_list, big_number_list, sign_list):
    while True:
        if check(small_number_list, sign_list):
            break
        if not next_permutation(small_number_list):
            break

    while True:
        if check(big_number_list, sign_list):   
            break
        if not prev_permutation(big_number_list):
            break
    print(''.join(big_number_list))
    print(''.join(small_number_list))

if __name__ == "__main__":
    N = int(input())
    result_list = list()
    sign_list = input().split(' ')
    small_number_list = [str(i) for i in range(0, N+1)]
    big_number_list = [str(i) for i in range(9, 9-N-1, -1)]
    solve(small_number_list, big_number_list, sign_list)