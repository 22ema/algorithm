
def tiling(number, save_list):
    save_list[1] = 1
    save_list[2] = 2
    for i in range(3, number+1):
        save_list[i] += save_list[i-1] + save_list[i-2]



if __name__ == "__main__":
    number = int(input())
    count = 0
    save_list = [0] * 10008
    tiling(number, save_list)
    print(save_list[number]%10007)