

def solution(array, commands):
    answer = list()
    for command in commands:
        wait_array = array[command[0]-1:command[1]]
        wait_array = sorted(wait_array)
        answer.append(wait_array[command[2]-1])
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = solution(array, commands)
    print(answer)