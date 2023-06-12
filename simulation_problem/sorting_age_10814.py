import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    person_list = list()
    for i in range(0, N):
        person = input().split(' ')
        person_list.append(person)
    person_list.sort(key = lambda x : (int(x[0])))
    for i in range(0, N):
        print(person_list[i][0], person_list[i][1])