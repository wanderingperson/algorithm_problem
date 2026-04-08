T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 인덱스 > 방향
# 0: 오른쪽 1: 아래 2 : 왼쪽 3 : 위쪽



for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    r = 0
    c = 0
    dir = 0

    for _ in range(N*N):
        dir = dir % 4
        arr[r][c] = _+1
        r+=dr[dir]
        c+=dc[dir]

        if(r >= N) or (r < 0) or (c < 0) or (c >= N) or arr[r][c] != 0: # 이 때 방향 전환
            r-=dr[dir]
            c-=dc[dir]
            dir+=1
            dir=dir%4
            r+=dr[dir]
            c+=dc[dir]
            
    print(f'#{tc}', end='')

    for _ in range(N):
        print()
        for i in range(N):
            print(arr[_][i], end=' ')
    print()