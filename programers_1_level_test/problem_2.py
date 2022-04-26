
def search(number, number_list):
    for i in range(0, len(number_list)):
        for j in range(0, len(number_list[0])):
            if number == number_list[i][j]:
                return i, j

def solution(numbers, hand):
    number_list = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   ['*', 0, '#']]
    right_hand_y = 2
    right_hand_x = 3
    left_hand_x = 3
    left_hand_y = 0
    result = ""
    for i in numbers:
        y, x = search(i, number_list)
        if i == 1 or i == 4 or i == 7:
            left_hand_x = x
            left_hand_y = y
            result += "L"
        elif i == 3 or i == 6 or i == 9:
            right_hand_x = x
            right_hand_y = y
            result += "R"
        else:
            rh_move_count = abs(right_hand_x-x) + abs(right_hand_y-y)
            lh_move_count = abs(left_hand_x-x) + abs(left_hand_y-y)
            print(lh_move_count, rh_move_count)
            if rh_move_count == lh_move_count:
                if hand == "right":
                    right_hand_x = x
                    right_hand_y = y
                    result += "R"
                elif hand == "left":
                    left_hand_x = x
                    left_hand_y = y
                    result += "L"
            elif rh_move_count > lh_move_count:
                left_hand_x = x
                left_hand_y = y
                result += "L"
            else:
                right_hand_x = x
                right_hand_y = y
                result += "R"
    return result


if __name__ == "__main__":
    a = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    b = "right"
    result = solution(a, b)
    print(result)