

flag = 0
def start_link(h_number, number_list, visited_list):
    for i in range(0, h_number):
        if visited_list[i] == True:


if __name__ == "__main__":
    human_number = int(input())
    number_list = [list(map(int, input().split())) for i in range(human_number)]
    visited_list = [False] * human_number
    start_team = [0]
    link_team = list()
    start_link(human_number, number_list, visited_list)