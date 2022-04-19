if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    Q = [4, 7]
    ans = 0
    while len(Q) > 1:
        F = Q[0]
        Q.pop(0)
        if F <= number_list[1]:
            if number_list[0]<= F:
                ans += 1
            Q.append(F*10+4)
            Q.append(F*10+7)
    print(ans)

