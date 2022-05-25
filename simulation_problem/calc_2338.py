
def sum(number_1, number_2):
    return number_1+number_2

def minus(number_1, number_2):
    return number_1-number_2

def multi(number_1, number_2):
    return number_1*number_2

if __name__=="__main__":
    number_1 = int(input())
    number_2 = int(input())
    print(sum(number_1, number_2))
    print(minus(number_1, number_2))
    print(multi(number_1, number_2))