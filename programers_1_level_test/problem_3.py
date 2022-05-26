
def solution(strings, n):
    for i in range(1, len(strings)):
        for j in range(0,i):
            if ord(strings[i][n]) < ord(strings[j][n]):
                temp = strings[i]
                strings[i] = strings[j]
                strings[j] = temp
            elif ord(strings[i][n]) == ord(strings[j][n]):
                if strings[i] < strings[j]:
                    temp = strings[i]
                    strings[i] = strings[j]
                    strings[j] = temp
    answer = strings

if __name__ == "__main__":
    strings = ["abce", "abcd", "cdx"]
    n = 2
    solution(strings, n )
    print(strings)