

def fill_tile(number):
    if number % 2 == 1:
        return 0
    else:
        result = [0] * 31
        result[2] = 3
        for i in range(4, number+1, 2):
            result[i] = result[i-2] * result[2]
            for j in range(i-4, -1, -2):
                result[i] += result[j] * 2
            result[i] += 2
        return result[number]

if __name__ == "__main__":

    number = int(input())
    answer = fill_tile(number)
    print(answer)