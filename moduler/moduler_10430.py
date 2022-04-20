if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    result_1 = (numbers[0]+numbers[1])%numbers[2]
    result_2 = ((numbers[0]%numbers[2])+(numbers[1]%numbers[2]))%numbers[2]
    result_3 = (numbers[0]*numbers[1])%numbers[2]
    result_4 = ((numbers[0]%numbers[2])*(numbers[1]%numbers[2]))%numbers[2]