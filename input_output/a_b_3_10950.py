
def add(x, y):
    return x+y
    
number = int(input())
for i in range(0, number):
    x, y = list(map(int, input().split(' ')))
    result = add(x, y)
    print(result)
        