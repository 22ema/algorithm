
def solution(s):
    answer = 0
    if s[0] == "+":
        answer = +1*int(s)
    elif s[0] == "-":
        answer = int(s)
    else :
        answer = int(s)
    return answer

if __name__ == "__main__":
    s = "-1234"
    answer = solution(s)
    print(answer)