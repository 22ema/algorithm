def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    number_list =list()
    count = 0
    i = 0
    while True:
        if i==0:
            number = '0'
        else:
            number = str(convert_notation(i, n))
        i += 1
        for j in number:
            if len(number_list) == t:
                answer = ''.join(number_list)
                return answer
            if count%m == (p-1):
                number_list.append(j)
            count += 1

if __name__ == "__main__":
    n = 16
    t = 16
    m = 2
    p = 1
    ans = solution(n, t, m, p)
    print(ans)