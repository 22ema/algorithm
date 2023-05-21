'''
6
10 20 15 25 10 20
10
   20
   30
      25
      35
         55
         40
            65
            35
'''


def up_stare(number, number_list):
    result_list = [0] * number
    if number <= 2:
        return sum(number_list)
    else:
        result_list[0] = number_list[0]
        result_list[1] = number_list[0] + number_list[1]
        for i in range(2, number):
            result_list[i] = max(result_list[i-3] + number_list[i-1] + number_list[i], result_list[i-2]+number_list[i])
        return result_list[-1]

if __name__ == "__main__":
    number = int(input())
    number_list = list()
    for i in range(0, number):
        score = int(input())
        number_list.append(score)
    answer = up_stare(number, number_list)
    print(answer)
    
