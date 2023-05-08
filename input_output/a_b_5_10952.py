
while True:
    input_ = input()
    if input_ == '0 0':
        break
    x, y = map(int, input_.split())
    print(x + y)