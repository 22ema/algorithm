'''
10
1 5 2 1 4 3 4 5 2 1
'''

def bitonic_numbers(number, number_list):
    reverse_number_list = number_list[::-1]
    result_list = [0] * number
    greatest_length = [0] * number
    smallest_length = [0] * number
    greatest_length[0] = 1
    smallest_length[0] = 1
    for i in range(1, number):
        greatest_length[i] = 1
        smallest_length[i] = 1
        for j in range(0, i):
            if number_list[i] > number_list[j] and greatest_length[i] < greatest_length[j] + 1:
                greatest_length[i] = greatest_length[j] + 1
            if reverse_number_list[i] > reverse_number_list[j] and smallest_length[i] < smallest_length[j] + 1:
                smallest_length[i] = smallest_length[j] + 1 
    smallest_length = smallest_length[::-1]
    for i in range(0, number):
        result_list[i] = smallest_length[i] + greatest_length[i]
    return max(result_list)-1

if __name__ == "__main__":
    number= int(input())
    number_list = list(map(int, input().split()))
    answer = bitonic_numbers(number, number_list)
    print(answer)
    
