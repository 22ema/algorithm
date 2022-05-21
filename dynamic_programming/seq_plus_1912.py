

def seq_plus(number, number_list, save_list):
    for i in range(1, number+1):
        if save_list[i-1]+number_list[i-1] < number_list[i-1]:
            save_list[i] = number_list[i-1]
        else:
            save_list[i] = number_list[i-1] + save_list[i-1]

if __name__ == "__main__":
    number = int(input())
    number_list = list(map(int, input().split()))
    save_list = [0] * (number+1)
    seq_plus(number, number_list, save_list)
    print(max(save_list[1:]))