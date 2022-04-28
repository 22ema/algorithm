
def solution(index, selected, N, M, save_list):
    if selected == M:               ## 만약 선택한 수가 M개면 출력 후 return
        print(save_list)
        return
    if index > N : return           ## 만약 index가 N보다 크다면 return
    save_list[selected] = index     ## save_list[] 배열 selected 위치에 index 저장
    solution(index+1, selected+1, N, M, save_list) ## index+1, selection+1 하여 solution 함수 호출
    save_list[selected] = 0         ## 함수 호출이 끝나면 selected 위치의 값 0 으로 변경
    solution(index+1, selected, N, M, save_list)    ## 현재 위치 save_list 수를 1더한다.


if __name__ == "__main__":
    number_list = list(map(int, input().split()))
    save_list = [0]*number_list[1]
    index = 1
    selected = 0
    solution(index, selected, number_list[0], number_list[1], save_list)

