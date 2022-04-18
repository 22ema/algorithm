def encoder(list_word, result_list):
    while True:
        count = 0
        for i in range(0,len(list_word)):
            if len(list_word[i]) == 0:
                count += 1
                pass
            else:
                result_list.append(list_word[i].pop(0))
        if count == 5:
            break
if __name__ == '__main__':
    list_word = list()
    result_list = list()
    for i in range(0,5):
        list_word.append(list(input()))
    print(list_word)
    encoder(list_word, result_list)
    for i in result_list:
        print(i,end="")

