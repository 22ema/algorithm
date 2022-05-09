def plus(number, sum, c):
    if number == sum:
        c += 1
        return c
    elif number <= sum:
        return c
    for i in range(1,4):
        sum += i
        c = plus(number, sum, c)
        sum -= i
    return c
if __name__ == "__main__":
    count = int(input())
    for i in range(count):
        number = int(input())
        sum = 0
        c = 0
        c = plus(number, sum, c)
        print(c)