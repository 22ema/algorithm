# 내가 푼 처음 방법
# if __name__ == "__main__":
#     number_str = input()
#     sentence = ""
#     for i in range(1, int(number_str)+1):
#         sentence += str(i)
#     print(len(sentence))

if __name__ == "__main__":
    number = int(input())
    plus_number = number
    result = 0
    count = 1
    test = 0
    while True:
        if plus_number // 10 > 0:
            plus_number = plus_number//10
            count += 1
        else:
            break
    for i in range(1, count):
        test += 9*(10**(i-1))
        result += 9*(10**(i-1))*i
    if count == 1:
        print(number)
    else:
        result += (number - test)*count
        print(result)

