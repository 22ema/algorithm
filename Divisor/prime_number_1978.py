if __name__=="__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    count = 0
    for i in number_list:
        flag = 0
        if i == 1:
            pass
        else:
            for j in range(2, int((i+1)**(1/2))+1):
                if i%j == 0:
                    flag = 1
                    break
            if flag == 0:
                count += 1
    print(count)