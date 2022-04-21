def calc(a, b):
    if b == 0:
        result = a
        return result
    else:
        return calc(b, a%b)

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    result = calc(numbers[0], numbers[1])
    print(result)
    print(numbers[0]*numbers[1]//result)