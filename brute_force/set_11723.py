import sys
def add(number, ans):
    ans = ans | 2**number
    return ans

def remove(number, ans):
    ans = ans & ~(2**number)
    return ans

def check(number, ans):
    n = ans & 2**number
    if n != 0:
        print(1)
    else:
        print(0)

def toggle(number, ans):
    ans = ans ^ 2**number
    return ans

def all():
    return ~0

def empty():
    return 0

if __name__ == "__main__":
    number = int(input())
    ans = 0
    for i in range(0, number):
        input_list = sys.stdin.readline().rstrip().split(" ")
        print(input_list[1])
        operator = input_list[0]
        if operator == "add":
            ans = add(int(input_list[1]), ans)
        elif operator == "remove":
            ans = remove(int(input_list[1]), ans)
        elif operator == "check":
            check(int(input_list[1]), ans)
        elif operator == "toggle":
            ans = toggle(int(input_list[1]), ans)
        elif operator == "all":
            ans = all()
        elif operator == "empty":
            ans = empty()

