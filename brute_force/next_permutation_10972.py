## 1. 뒤에서 부터 현재 순열의 정렬 상태 확인
## 2. 만약 앞의 수가 뒤에 오는 수보다 작으면 swap
## 3. 뒤에 오는 수들 역 수로 변경
def next_perm(number, number_list):
    for i in range(number-1, 0, -1):
        if number_list[i] > number_list[i-1]:
            min = i
            for j in range(i, number):
                if number_list[j] < number_list[min] and number_list[j] > number_list[i-1]:
                    min = j
            temp = number_list[min]
            number_list[min] = number_list[i-1]
            number_list[i-1] = temp
            number_list[i:] = sorted(number_list[i:])
            return number_list
        else:
            pass
    return -1


if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    number_list = next_perm(number, number_list)
    if number_list == -1:
        print(number_list)
    else:
        for i in number_list:
            print(i, end=" ")