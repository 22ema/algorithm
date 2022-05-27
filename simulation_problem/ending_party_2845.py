


if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    people_number = list(map(int, input().split()))
    ans = number_list[0]*number_list[1]
    for i in people_number:
        print(i-ans, end=" ")