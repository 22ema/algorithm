

def solution(answers):
    answer = list()
    p_count_list = [0] * 3
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    for i in range(0, len(answers)):
        if p1[i] == answers[i]:
            p_count_list[0] += 1
        if p2[i] == answers[i]:
            p_count_list[1] += 1
        if p3[i] == answers[i]:
            p_count_list[2] += 1
    max_c = max(p_count_list)
    for i in range(0, len(p_count_list)):
        if max_c == p_count_list[i]:
            answer.append(i+1)
    return answer

if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5]
    ans = solution(answers)
    print(ans)