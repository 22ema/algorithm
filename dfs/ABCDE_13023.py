


import sys

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    edges = list()
    a = [[False] * numbers[0] for _ in range(numbers[0])]
    g = [[] for _ in range(numbers[0])]
    for i in range(numbers[1]):
        relate = list(map(int, input().split()))
        edges.append((relate[0], relate[1]))
        edges.append((relate[1], relate[0]))
        a[relate[0]][relate[1]] = a[relate[1]][relate[0]] = True
        g[relate[0]].append(relate[1])
        g[relate[1]].append(relate[0])
    numbers[1] *= 2
    for i in range(numbers[1]):
        for j in range(numbers[1]):
            A, B = edges[i]
            C, D = edges[j]
            if A == B or A==C or A==D or B==C or B==D or C==D:
                continue
            if not a[B][C]:
                continue
            for E in g[D]:
                if A==E or B==E or C== E or D==E:
                    continue
                print(1)
                sys.exit(0)
    print(0)