
def max_money(card_number, card_value_list, money_list):
    money_list[1] = card_value_list[0]
    for i in range(2, card_number+1):
        for j in range(0, i):
            if money_list[i-(j+1)] == 10000:
                temp = card_value_list[j]
            else:
                temp = money_list[i-(j+1)]+card_value_list[j]
            if temp < money_list[i]:
                money_list[i] = temp

if __name__ == "__main__":
    card_number = int(input())
    card_value_list = list(map(int, input().split()))
    money_list = [10000] * (card_number+1)
    max_money(card_number, card_value_list, money_list)
    print(money_list[card_number])