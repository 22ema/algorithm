if __name__ == "__main__":
    character = '가'
    list_char = ['가', '가나', '가나다', '나다']
    result = list()
    for x in list_char:
        if character in x:
            result.append(x)
    print(result)
