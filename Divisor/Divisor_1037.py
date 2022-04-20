# def sorting(numbers_list):
#     for i in range(0, len(numbers_list)):
#         for j in range(i, len(numbers_list)):
#             if numbers_list[i]>numbers_list[j]:
#                 temp = numbers_list[i]
#                 numbers_list[i] = numbers_list[j]
#                 numbers_list[j] = temp
#     return numbers_list

if __name__ == "__main__":
    number = int(input())
    numbers_list = list(map(int, input().split()))
    result = min(numbers_list)*max(numbers_list)
    print(result)