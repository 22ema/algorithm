
if __name__ == "__main__":
    number = int(input())
    error_number = int(input())
    if error_number == 0:
        print(len(list(str(number))))
    else :
        errors = list(map(int, input().split()))
        all_list = list()
        right_list =list()
        if error_number == 10:
            print(abs(number - 100))
        elif number == 100:
            print(0)
        else :
            for i in range(0, 1000001):
                all_list.append(list(map(int, str(i))))
            for i in all_list:
                for j in range(0, len(i)):
                    if i[j] in errors:
                        break
                    elif j == len(i)-1:
                        right_list.append(i)
            result_list = list()
            for i in right_list:
                number_s = 0
                for j in range(0, len(i)):
                    number_s += i[j]*(10**(len(i)-1-j))
                result_list.append(number_s)
            min = abs(number-result_list[0])
            minimum_number = result_list[0]
            for i in range(1, len(result_list)):
                if min > abs(result_list[i]-number):
                    min = abs(result_list[i]-number)
                    minimum_number = result_list[i]
            minimum = min+len(list(str(minimum_number)))
            if abs(number - 100) < minimum:
                print(abs(number - 100))
            else:
                print(minimum)

