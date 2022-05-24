
def split_money(M, N):
    sep_money = M%N
    number = M//N
    print(number)
    print(sep_money)

if __name__=="__main__":
    numbers = list(map(int, input().split()))
    split_money(numbers[0], numbers[1])