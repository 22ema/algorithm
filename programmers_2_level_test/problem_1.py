MAX = 10000000

def aristoteles_num(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def number_list(index, numbers, save_list, visited_list, result_list):
    if index == len(numbers):
        return 0
    for i in range(0, len(numbers)):
        if visited_list[i] == True:
            continue
        save_list.append(numbers[i])
        visited_list[i] = True
        if ''.join(save_list) in result_list or save_list[0] == '0':
            pass
        else:
            result_list.append(''.join(save_list))
        print(result_list)
        number_list(index+1, numbers, save_list, visited_list, result_list)
        visited_list[i] = False
        save_list.pop()

def solution(numbers):
    answer = 0
    prime_nums = aristoteles_num(MAX)
    numbers = list(numbers)
    save_list = list()
    visited_list = [False] * len(numbers)
    result_list = list()
    number_list(0, numbers, save_list, visited_list, result_list)
    for i in result_list:
        print(i)
        if int(i) in prime_nums:
            answer+=1
    return answer

if __name__ == "__main__":
    numbers = "011"
    ans = solution(numbers)
    print(ans)
