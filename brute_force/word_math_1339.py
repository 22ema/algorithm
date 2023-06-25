
def next_permutation(a):
    i = len(number_list) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

## dictionary로 만들어서 index를 알파벳으로 하여 체크하면 될듯함
def check(words_list, letters, number_list):
    m = len(letters)
    ans = 0
    alpha = dict()
    for i in range(0, m):
        alpha[letters[i]] = number_list[i]
    for s in words_list:
        now = 0
        for x in s:
            now = now * 10 + alpha[x]
        ans += now
    return ans


if __name__ == "__main__":
    N = int(input())
    words_list = list()
    letters = set()
    for i in range(0, N):
        words = input()
        words_list.append(words)
        letters |= set(words)
    letters = list(letters)
    number_list = [i for i in range(9, 9-len(letters), -1)]
    number_list.sort()
    ans = 0
    while True: 
        now = check(words_list, letters, number_list)
        if ans < now :
            ans = now
        if not next_permutation(number_list):
            break
    print(ans)

