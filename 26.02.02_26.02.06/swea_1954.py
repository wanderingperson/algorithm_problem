T = int(input())

dr = [0,1,0,-1] # 행의 값 변경하기 위한 dr
dc = [1,0,-1,0] # 열의 값 변경하기 위한 dc
switch = 0 # 말그대로 스위치


for tc in range(1, T+1): 
    

    tyle = int(input()) # tyle*tyle을 생성하기 위해 크기를 입력받음
    arr = [[0]*tyle for _ in range(tyle)] # 0이들어있는상태로 tyle*tyle리스트 생성

    r = 0 
    c = -1
    # arr[r][c]=1 # 시작점에 1을 할당

    for digit in range(1,tyle*tyle+1): # 1은 이미 할당을 했으므로 2~tyle*tyle까지
        if (0 <= r+dr[switch] < tyle) and (0 <= c+dc[switch] < tyle) and (arr[r+dr[switch]][c+dc[switch]] == 0): # 만약 사전이동을 해봤는데 범위를 안벗어나고, 기존값을덮어씌우지 않는다면
            r = r+dr[switch] # r의 좌표값을 변경
            c = c+dc[switch] # c의 좌표값을 변경
            arr[r][c] = digit # 현재 좌표값에 digit값을 할당
        else: # 만약 범위를 벗어나거나 기존값을 덮어씌운다면
            switch = (switch+1)%4 # switch값을 변경(방향을 변경)
            r = r+dr[switch] # r의 좌표값을 변경
            c = c+dc[switch] # c의 좌표값을 변경
            arr[r][c] = digit # 현재 좌표값에 digit값을 할당



    print(f'#{tc}')
    for row in arr:
        print(*row)