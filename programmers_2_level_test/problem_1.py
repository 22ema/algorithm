
def number_124(n, number_list):
    for i in range(1, n+1):
        if i == 1:
            number_list[i] = '1'
        elif i == 2:
            number_list[i] = '2'
        elif i == 3:
            number_list[i] = '4'
        else:
            number_list[i] = number_list[(i-1)//3] + number_list[((i-1)%3)+1]






def solution(n):
    number_list = [''] * (n+1)
    number_124(n, number_list)
    answer = number_list[n]
    return answer

if __name__ == "__main__":
    n = 4
    answer = solution(n)
    print(answer)