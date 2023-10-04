from collections import deque

number = int(input())
test_case = list()


for _ in range(number):
    inp = list(map(int, input().split(' ')))
    test_case.append(inp)
for case in test_case:
    visit = [False] * 10000
    result = None
    dq = deque()
    dq.append([case[0],''])
    while dq:
        a = dq.popleft()
        if a[0] == case[1]:
            answer = a[1]
            dq.clear()
            break
        num2 = int((2*a[0]) % 10000)
        if not visit[num2]:
            dq.append([num2, a[1]+'D'])
            visit[num2] = True
        num2 = (a[0]-1)
        if num2 == -1:
            num2 = 9999
        if not visit[num2]:
            dq.append([num2, a[1]+'S'])
            visit[num2] = True
        num2 = ((a[0] % 1000)* 10) +(a[0]//1000)
        if not visit[num2]:
            dq.append([num2, a[1]+'L'])
            visit[num2] = True
        
        num2 = ((a[0]%10)*1000)+(a[0]//10)
    
        if not visit[num2]:
            dq.append([num2, a[1]+'R'])
            visit[num2] = True
    print(answer)
        