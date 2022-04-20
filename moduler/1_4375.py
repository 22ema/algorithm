if __name__ == "__main__":
    while True:
        try:
            number = int(input())
        except:
            break
        count = 1
        result = 1
        while True:
            if result % number == 0:
                break
            count += 1
            result = result * 10 + 1
        print(count)