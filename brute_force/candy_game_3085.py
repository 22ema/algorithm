
def search_candy_row(candy_list,visited_list, number, i, j, count):
    visited_list[i][j] = True
    if j+1 < number and candy_list[i][j] == candy_list[i][j+1] and visited_list[i][j+1] == False:
        count += 1
        count = search_candy_row(candy_list,visited_list, number, i, j+1, count)
    if 0 <= j-1 and candy_list[i][j] == candy_list[i][j-1] and visited_list[i][j-1] == False:
        count += 1
        count = search_candy_row(candy_list,visited_list, number, i, j-1, count)
    return count

def search_candy_col(candy_list, visited_list, number, i, j, count):
    visited_list[i][j] = True
    if i + 1 < number and candy_list[i][j] == candy_list[i+1][j] and visited_list[i+1][j] == False:
        count += 1
        count = search_candy_col(candy_list, visited_list, number, i+1, j, count)
    if 0 <= i-1 and candy_list[i][j] == candy_list[i-1][j] and visited_list[i-1][j] == False:
        count += 1
        count = search_candy_col(candy_list, visited_list, number, i-1, j, count)
    return count


def swap(i, j, k, l, candy_list):
    temp = candy_list[i][j]
    candy_list[i][j] = candy_list[k][l]
    candy_list[k][l] = temp
    return candy_list

if __name__ == "__main__":
    number = int(input())
    candy_list = [list(input()) for _ in range(0, number)]
    max_num = 0
    for i in range(0, number):
        for j in range(0, number):
            visited_list = [[False] * number for _ in range(0, number)]
            row_count = 1
            row_count = search_candy_row(candy_list,visited_list, number, i, j, row_count)
            visited_list = [[False] * number for _ in range(0, number)]
            col_count = 1
            col_count = search_candy_col(candy_list, visited_list, number, i, j, col_count)
            if row_count > max_num:
                max_num = row_count
            if col_count > max_num:
                max_num = col_count
    x = [1, 0]
    y = [0, 1]
    for i in range(0, number):
        for j in range(0, number):
            if i+1 < number:
                candy_list = swap(i, j, i+1, j, candy_list)

                row_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                row_count = search_candy_row(candy_list, visited_list, number, i, j, row_count)
                col_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                col_count = search_candy_col(candy_list, visited_list, number, i, j, col_count)
                if row_count > max_num:
                    max_num = row_count
                if col_count > max_num:
                    max_num = col_count
                row_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                row_count = search_candy_row(candy_list, visited_list, number, i+1, j, row_count)
                col_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                col_count = search_candy_col(candy_list, visited_list, number, i+1, j, col_count)
                if row_count > max_num:
                    max_num = row_count
                if col_count > max_num:
                    max_num = col_count

                candy_list = swap(i+1, j, i, j, candy_list)


            if j+1 < number:
                candy_list = swap(i, j, i, j+1, candy_list)

                row_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                row_count = search_candy_row(candy_list, visited_list, number, i, j, row_count)
                col_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                col_count = search_candy_col(candy_list, visited_list, number, i, j, col_count)
                if row_count > max_num:
                    max_num = row_count
                if col_count > max_num:
                    max_num = col_count
                row_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                row_count = search_candy_row(candy_list, visited_list, number, i, j+1, row_count)
                col_count = 1
                visited_list = [[False] * number for _ in range(0, number)]
                col_count = search_candy_col(candy_list, visited_list, number, i, j+1, col_count)
                if row_count > max_num:
                    max_num = row_count
                if col_count > max_num:
                    max_num = col_count

                candy_list = swap(i, j+1, i, j, candy_list)

    print(max_num)