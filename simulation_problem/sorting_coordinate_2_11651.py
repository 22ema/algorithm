import sys

input = sys.stdin.readline

def sort_coor(coor, N):
    coor.sort(key = lambda x : (x[1], x[0]))
    return coor

if __name__ == "__main__":
    N = int(input())
    coor = list()
    for i in range(0, N):
        xy = list(map(int, input().split()))
        coor.append(xy)
    
    answer = sort_coor(coor, N)
    for i in range(0, N):
        print(answer[i][0], answer[i][1])