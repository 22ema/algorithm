

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    count = 0
    index_dict = dict()
    id_dict = dict()
    count_dict = dict()
    for i in id_list:
        id_dict[i] = list()
        index_dict[i] = count
        count+=1
        count_dict[i] = 0
    for i in report:
        n, m = i.split(" ")
        if n in id_dict[m]:
            pass
        else:
            id_dict[m].append(n)
            count_dict[m] += 1
    for index , value in count_dict.items():
        if value >= k:
            for i in id_dict[index]:
                answer[index_dict[i]] += 1
    return answer

if __name__ == "__main__":
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 2
    ans = solution(id_list, report, k)
    print(ans)