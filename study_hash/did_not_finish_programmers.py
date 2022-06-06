import collections

def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    print(participant)
    print(completion)
    for i in range(0, len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
        elif i == len(completion)-1:
            return participant[-1]




if __name__ == "__main__":
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    ans_list = solution(participant, completion)
    print(ans_list)