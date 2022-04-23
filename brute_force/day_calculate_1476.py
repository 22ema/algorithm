if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    count = 0
    x = 0
    y = 0
    z = 0
    while True:
        count +=1
        x +=1
        y +=1
        z +=1
        if x == 16:
            x = 1
        if y == 29:
            y = 1
        if z == 20:
            z = 1
        if number_list[0] == x and number_list[1] == y and number_list[2] == z:
            print(count)
            break

