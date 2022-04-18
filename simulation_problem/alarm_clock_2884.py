
if __name__ == "__main__":
    time_list = list(map(int, input().split()))
    hour = time_list[0]
    minute = time_list[1]

    if minute < 45:
        minute = 60 - (45 - minute)
        if hour == 0:
            hour = 23
        else:
            hour -= 1
    else :
        minute -= 45
    print("{} {}".format(hour, minute))