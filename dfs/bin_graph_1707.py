import sys
sys.setrecursionlimit(1000000)
def dfs(index, number_list, visited_list, flag):
    visited_list[index] = flag
    for i in range(0, len(number_list[index])):
        if visited_list[number_list[index][i]] == 0:
            if not dfs(number_list[index][i], number_list, visited_list, 3-flag):
                return False
        elif visited_list[number_list[index][i]] == visited_list[index]:
            return False
    return True


if __name__ == "__main__":
    count = int(input())

    for i in range(0, count):
        v, e = map(int , sys.stdin.readline().split())
        number_list = [[] for _ in range(v)]
        visited_list = [0] * v
        for j in range(0, e):
            a, b = map(int , sys.stdin.readline().split())
            number_list[a-1].append(b-1)
            number_list[b-1].append(a-1)
        result = "YES"
        flag = 1
        for i in range(0, v):
            if visited_list[i] == 0:
                if not dfs(i, number_list, visited_list, flag):
                    result = False
        print('YES' if result else 'NO')