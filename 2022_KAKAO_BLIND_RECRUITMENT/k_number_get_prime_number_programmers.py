import math
def primers(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if 0 == number % i:
            return False
    return True

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]

def solution(n, k):
    number = convert(n, k)
    count = 0
    number_str = str(number)
    number_list = number_str.split("0")
    n_list = list()
    for i in number_list:
        if i != '':
            n_list.append(i)
    n_list = list(map(int, n_list))
    for i in n_list:
        if primers(i):
            count += 1
    return count



if __name__ == "__main__":
    n = 437674
    k = 3
    count = solution(n, k)
    print(count)