
def square_number(number, save_list):
    for i in range(1, number+1):
        save_list[i] = i
        j = 1
        while i >= j*j:
            if save_list[i] > save_list[i-j*j]+1:
                save_list[i] = save_list[i-j*j]+1
            j+=1

if __name__ == "__main__":
    number = int(input())
    save_list = [0] * (number+1)
    square_number(number, save_list)
    print(save_list[number])