

if __name__ == "__main__":
    while True:
        N, M = list(map(int, input().split()))
        if N == 0 and M == 0:
            break
        if N > M:
            print("Yes")
        else:
            print("No")