
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(0, len(phone_book)-2):
        if phone_book[i] in phone_book[i+1] or phone_book[i] in phone_book[i+2] or phone_book[i+1] in phone_book[i+2]:
            return False
    return True



if __name__ == "__main__":
    phone_book = ["12","123","1235","567","88"]
    answer = solution(phone_book)
    print(answer)