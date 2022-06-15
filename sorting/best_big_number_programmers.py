

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*2, reverse=True)
    return str(int(''.join(numbers)))



if __name__ == "__main__":
    numbers = [3, 30, 34, 5, 9]
    answer = solution(numbers)
    print(answer)