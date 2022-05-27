


if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    sum = 0
    for i in number_list:
        sum += i*i
    result = sum%10
    print(result)