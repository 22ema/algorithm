
def make_pw(index, start, N, chars, visited_list, selected_list):
    a_count = 0
    b_count = 0
    if index == N:
        for i in selected_list:
            if i in "aeiou":
                a_count += 1
            if i in "bcdfghjklmnpqrstvwxyz":
                b_count += 1
        if a_count >= 1 and b_count >= 2:
            for i in selected_list:
                print(i, end='')
            print()
        return 0
    for i in range(start, len(chars)):
        if visited_list[i] == True:
            continue
        visited_list[i] = True
        selected_list[index] = chars[i]
        make_pw(index+1, i, N, chars, visited_list, selected_list)
        visited_list[i] = False


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    chars = list(input().split())
    visited_list = [False] * numbers[1]
    index = 0
    start = 0
    selected_list = [0]*numbers[0]
    chars = sorted(chars)
    make_pw(index, start, numbers[0], chars, visited_list, selected_list)