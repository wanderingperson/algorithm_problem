T = int(input())

dr = [1,-1,0,0]
dc = [0,0,1,-1]


for tc in range(1,T+1):
    N = int(input())

    square = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):

            if square[r][c]==2:
                for direction in range(4):
                    for i in range(1,N):
                        nr = r + dr[direction]*i
                        nc = c + dc[direction]*i
                        if (0<=nr<N) and (0<=nc<N):
                            if square[nr][nc]==1:
                                break
                            square[nr][nc]=3

    count=0
    for r in range(N):
        for c in range(N):
            if square[r][c]==0:
                count+=1

    print(f'#{tc} {count}')
    #인덱스를 벗어나거나, 1을 만날때까지

