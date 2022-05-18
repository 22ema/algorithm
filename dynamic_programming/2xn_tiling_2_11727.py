
def tiling(number, save_list):
    save_list[1] = 1
    if number >= 2:
        save_list[2] = 3
        for i in range(3, number+1):
            save_list[i] = save_list[i-1] + (2 * save_list[i-2])

if __name__ == "__main__":
    number = int(input())
    save_list = [0] * (number+1)
    tiling(number, save_list)
    print(save_list[number]%10007)