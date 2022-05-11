
def start_link(index, num_list, start, link,ans):
    if index == len(num_list):
        start_sum = 0
        link_sum =0
        if len(start) != len(num_list)//2:
            return ans
        if len(link) != len(num_list)//2:
            return ans
        for i in range(len(num_list)//2):
            for j in range(len(num_list)//2):
                start_sum += num_list[start[i]][start[j]]
                link_sum += num_list[link[i]][link[j]]
        temp = abs(start_sum - link_sum)
        if ans == -1 or ans > temp :
            ans = temp
        return ans
    ans = start_link(index +1, num_list, start+[index], link, ans)
    ans = start_link(index +1, num_list, start, link+[index], ans)
    return ans

if __name__ == "__main__":
    numbers = int(input())
    number_list = [list(map(int, input().split())) for i in range(numbers)]
    start = list()
    link = list()
    ans = -1
    result = start_link(0, number_list, start, link, ans)
    print(result)
