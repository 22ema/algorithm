
def gu_gu_dan(number):
    for i in range(1, 10):
        print("{} * {} = {}".format(number,i,number*i))

if __name__ == "__main__":
    number = int(input())
    gu_gu_dan(number)