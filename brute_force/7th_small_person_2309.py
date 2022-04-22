## 9명중 7명을 찾기
## 9명중에 2명을 찾기 oo

def sorting(number_list):
    for i in range(0, 7):
        for j in range(i, 7):
            if number_list[j] <= number_list[i]:
                temp = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = temp
    return number_list
def search(number_list):
    for i in range(0, 9):
        for j in range(0, 9):
            result = 0
            result_list = list()
            if j==i:
                pass
            else:
                for z in range(0,9):
                    if z==i or z==j:
                        pass
                    else:
                        result_list.append(number_list[z])
                        result+=number_list[z]
            if result == 100:
                return result_list

if __name__ == "__main__":
    number_list = list()
    visited_list = [False] * 9
    for i in range(0,9):
        number = int(input())
        number_list.append(number)
    result_list = search(number_list)
    result_list = sorting(result_list)
    for i in result_list:
        print(i)