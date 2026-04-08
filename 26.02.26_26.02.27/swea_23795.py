dr = [1,-1,0,0]
dc = [0,0,1,-1]

def lazer(r,c):
    #4방향 델타
    for i in range(4):

        #끝까지 뻗어나가기(괴물이 있는곳은 수정안하게 1부터 시작)
        for j in range(1, N):
            nr = r + dr[i]*j
            nc = c + dc[i]*j
            
            # 범위 안이고
            if (0<=nr<N) and (0<=nc<N):
                # 벽하고 맞닿으면 바로 종료
                if safe_zone[nr][nc]==1:
                    break

                # 광선이 닿는곳을 3으로 변경
                safe_zone[nr][nc]=3



T = int(input())


for tc in range(1,T+1):
    N = int(input())

    safe_zone = [list(map(int, input().split())) for _ in range(N)]

    # 괴물이 있는곳에서 lazer함수 실행
    for r in range(N):
        for c in range(N):
            if safe_zone[r][c]==2:
                lazer(r,c)

    # 좌표값이 0인곳을 count하기
    safe_count=0
    for r in range(N):
        for c in range(N):
            if safe_zone[r][c]==0:
                safe_count+=1
    print(f'#{tc} {safe_count}')