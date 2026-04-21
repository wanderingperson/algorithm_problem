dr = [1,-1,0,0]
dc = [0,0,1,-1]

# idx : 지금 고려중이 코어의 인덱스
# core_cnt : 지금까지 연결된 코어의 수
# wire_len : 지금까지 사용된 전선의 길이
def dfs(idx, core_cnt, wire_len):
    global max_core, min_len

    # 지금까지 연결된 코어수와 앞으로 남은 코어수가 max_core보다 작다면(남은 코어들을 전부 연결했다고 가정하면)
    if core_cnt + (len(cores)-idx)<max_core:
        return
    
    if idx == len(cores):
        if core_cnt>max_core:
            max_core=core_cnt
            min_len=wire_len
        elif core_cnt==max_core:
            min_len=min(min_len, wire_len)
        return
    
    r,c = cores[idx]

    for dir in range(4):
        nr, nc = r,c
        length = 0

        # 연결 가능한지 확인
        while True:
            nr+=dr[dir]
            nc+=dc[dir]

            # 범위밖이면 스킵
            if nr<0 or nr>=N or nc<0 or nc>=N:
                break
            
            #전선이나 코어로 가로막혀있을때
            if cell[nr][nc]!=0:
                length=0
                break

            length+=1

        if length==0:
            continue

        nr, nc = r, c

        for _ in range(length):
            nr+=dr[dir]
            nc+=dc[dir]
            cell[nr][nc]=2
        dfs(idx+1, core_cnt+1, wire_len+length)

        nr, nc = r, c

        for _ in range(length):
            nr+=dr[dir]
            nc+=dc[dir]
            cell[nr][nc]=0
    # 연결 안한 케이스
    dfs(idx+1, core_cnt, wire_len)



T = int(input())

for tc in range(1,T+1):
    N=int(input())
    cell = [list(map(int,input().split())) for _ in range(N)]

    cores = []

    for i in range(N):
        for j in range(N):
            if cell[i][j]==1:
                if i==0 or i==N-1 or j==0 or j==N-1:
                    continue
                # 바뀌지 않을 좌표는 튜플로 저장하는게 훨 나음(코어의 위치는 고정)
                cores.append((i,j))

    max_core = 0
    min_len = N**2

    dfs(0,0,0)

    print(f'#{tc} {min_len}')