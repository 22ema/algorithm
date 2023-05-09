number = int(input())

for i in range(0, number):
    x, y = map(int, input().split())
    print(f"Case #{i+1}: {x} + {y} = {x+y}")