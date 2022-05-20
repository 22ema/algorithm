
def very_long(number, number_list, save_list):
    for i in range(1, number+1):
        save_list[i] = 1
        for j in range(1, i):
            if number_list[i-1] > number_list[j-1] and save_list[i] < (save_list[j]+1):
                save_list[i] = save_list[j] + 1

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    save_list = [0] * (number+1)
    very_long(number, number_list, save_list)
    print(max(save_list))