
def solution(a, b):
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED","THU"]
    days = 0
    if a == 1:
        day = b%7
        ans = day_list[day-1]
    else:
        for i in range(1, a+1):
            if i == a:
                days += b
                day = days%7
                ans=day_list[day-1]
                break
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i==10 or i==12:
                days += 31
            elif i == 4 or i == 6 or i == 9 or i == 11:
                days += 30
            else:
                days += 29

    return ans

if __name__ == "__main__":
    a = 5
    b = 24
    result = solution(a, b)
    print(result)