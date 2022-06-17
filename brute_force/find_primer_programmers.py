
def primers(max_num):
    visited_list = [False] * (max_num+1)
    visited_list[0] = True
    visited_list[1] = True
    result_list = list()
    for i in range(0, max_num+1):
        if visited_list[i] == True:
            continue
        result_list.append(i)
        check = i
        count = 2
        while check <= max_num:
            visited_list[check] = True
            check = i * count
            count += 1
    return result_list




def brute(numbers, visited_list, save_str, result):

    for i in range(0, len(numbers)):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        save_str = save_str + numbers[i]
        if save_str[0] == '0':
            save_str = save_str[1:]
        if save_str in result:
            pass
        elif save_str!='':
            result.append(save_str)
        brute(numbers, visited_list, save_str , result)
        save_str = save_str[:-1]
        visited_list[i] = False
    return 0


def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    visited_list = [False] * len(numbers)
    save_str = ""
    result_list = list()
    brute(numbers, visited_list, save_str,result_list)
    result_list = list(map(int, result_list))

    max_num = max(result_list)
    prime_list=primers(max_num)
    for i in result_list:
        if i in prime_list:
            answer +=1
    return answer


if __name__ == "__main__":
    numbers = "011"
    ans = solution(numbers)
    print(ans)