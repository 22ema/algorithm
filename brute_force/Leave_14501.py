
def do_consulting(index, numbers_list):
    if index == len(numbers_list):
        print("test")


if __name__ == "__main__":
    count = int(input())
    numbers_list = list()
    index = 0
    for i in range(count):
        numbers_list.append(list(map(int, input().split())))
    do_consulting(index, numbers_list)