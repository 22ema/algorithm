import sys

input = sys.stdin.readline

if __name__ == "__main__":
    number_count = int(input())
    number_list = list()
    for i in range(0, number_count):
        number = int(input())
        number_list.append(number)
    number_list = sorted(number_list,reverse=False)
    for i in range(0, number_count):
        print(number_list[i])