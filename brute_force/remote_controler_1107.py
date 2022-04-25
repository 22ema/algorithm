def possible(i, broken):
    if i == 0:
        if broken[0]==False:
            return 1
        else:
            return 0
    l=0
    while i>0:
        if broken[i%10] == True:
            return 0
        l += 1
        i //= 10
    return l


if __name__ == "__main__":
    channel_number = int(input())
    error_number = int(input())
    if error_number > 0:
        errors = list(map(int, input().split()))
    else:
        errors = []
    broken = [False]*10
    for x in errors:
        broken[x] = True
    ans = abs(channel_number-100)
    for i in range(0, 1000001):
        l = possible(i, broken)
        if l>0:
            press = abs(i-channel_number)
            if ans > l+press:
                ans = l+press
    print(ans)



