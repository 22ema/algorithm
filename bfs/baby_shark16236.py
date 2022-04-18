import sys, collections

def bfs(shark_x, shark_y, shark_size):
    q = collections.deque([(shark_x, shark_y, 0)])    ## [shark_x, shark_y, 0]
    dist_list = []                                  ## dist_list 빈배열 생성
    visited = [[False]*n for _ in range(n)]     ## visited 배열 생성
    visited[shark_x][shark_y] = True            ## shark_x와 shark_y(현재 shark의 index)는 방문처리
    min_dist = int(1e9)
    count = 0
    while q:
        x, y, dist = q.popleft()                ## queue 내 데이터 선입선출
        for i in range(4):                      ## 상하좌우 확인
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:     ## xx와 yy가 0과 n 사이에 있으며 xx와 yy 좌표를 방문하지 않은 경우
                if board[xx][yy] <= shark_size:                         ## board[xx][yy]가 상어 크기보다 작다면
                    visited[xx][yy] = True                              ## 방문 체크
                    if 0 < board[xx][yy] < shark_size:                  ## 만약 현재 상어 사이즈보다 작다면
                        min_dist = dist                               ## 왜 min_dist에 dist를 저장?
                        dist_list.append((dist+1, xx, yy))              ## dist_list에 dist+1, xx, yy 추가
                        print("eat :", xx, yy, str(board[xx][yy]))
                    if dist+1 <= min_dist:                              ## dist+1 <= mindist 인경우
                        q.append((xx, yy, dist+1))
                        print("move:", xx, yy, str(board[xx][yy]))
    if dist_list:                                                       ## 해당 코드로 분기되기 위한 조건은 모든 배열 체크 완료 또는 현재 물고기 위치 주변에 큰수 밖에 없는 경우
        dist_list.sort()
        print("dist:",dist_list[0])
        return dist_list[0]
    else:
        return False



if __name__ == "__main__":
    shark_x, shark_y = 0, 0 ## shark의 좌표
    shark_size = 2          ## shark의 size
    eat_cnt = 0             ## 먹은 횟수

    fish_cnt = 0
    fish_pos = []
    time = 0

    dx = (0, 0, 1, -1)      ## what is this?
    dy = (1, -1, 0, 0)      ## what is this?

    n = int(input())   ## NxN 크기의 공간 입력받기.
    board = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if 0<board[i][j] <= 6:      ## 배열의 i, j위치에 물고기가 있는경우
                fish_cnt += 1           ## count +=1
                fish_pos.append((i,j))  ## fish의 위치를 fish_pos 배열에 추가
            elif board[i][j] == 9:      ## baby shark의 위치를 찾는다.
                shark_x, shark_y = i, j ## baby shark의 배열 index를 저장
    board[shark_x][shark_y] = 0         ## baby_shark index내 value를 0으로 초기화

    while fish_cnt:                     ## 물고기 수만큼 반복
        result = bfs(shark_x, shark_y, shark_size)  ## bfs 함수 호출
        if not result:
            break
        shark_x, shark_y = result[1], result[2]
        time += result[0]
        eat_cnt += 1
        fish_cnt -= 1
        if shark_size == eat_cnt:
            shark_size += 1
            eat_cnt = 0
        board[shark_x][shark_y] = 0
    print(time)