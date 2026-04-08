from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


# bfs에 대한 정의
def bfs(r, c, visited): #해당r,c좌표, visited는 일단 지금 의미없음
    q = deque()
    # 해당r,c좌표를 q에 추가하고 방문으로 처리하기
    q.append((r,c))
    visited[r][c] = True

    # q에 값이 있다면
    while q:
        # 현재r과 현재c에 q에서 popleft한걸 할당하고
        cr, cc = q.popleft()

        # 상하좌우를 확인
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 리스트 범위내인지 확인하기
            if 0<=nr<R and 0<=nc<C:

                # 해당얼음값이 0초과고 미방문상태라면
                if iceage[nr][nc] > 0 and not visited[nr][nc]:
                    # 방문으로 바꾸고 q에 nr,nc값을 추가하기
                    visited[nr][nc] = 1
                    q.append((nr,nc))

# 얼음 덩어리 세기
def count_ice():
    # 처음엔 전부 미방문으로 설정하기
    visited = [[0]*C for _ in range(R)]
    # count는 0부터 시작
    count = 0

    #r,c가 미방문상태고 0초과라면 count를 1한다.
    for r in range(R):
        for c in range(C):
            if iceage[r][c] > 0 and not visited[r][c]:
                bfs(r, c, visited)
                count += 1

    return count


def melt():
    melt_amount = [[0]*C for _ in range(R)]

    # iceage의 값이 1이상인곳을 탐색 후 상하좌우의 바닷물만큼 count
    for r in range(R):
        for c in range(C):
            if iceage[r][c] > 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<R and 0<=nc<C:
                        if iceage[nr][nc] == 0:
                            melt_amount[r][c] += 1

    # 이후 바닷물양만큼을 iceage에서 뺀다. 0밑으로 내려갈시 0으로 설정
    for r in range(R):
        for c in range(C):
            iceage[r][c] = max(0, iceage[r][c] - melt_amount[r][c])

# R, C를 입력받고 해당배열의 크기에 알맞게 리스트에 값을 넣는다
R, C = map(int, input().split())
iceage = [list(map(int, input().split())) for _ in range(R)]

# 0년차부터 시작
year = 0

# 2덩어리 이상이 되거나 0덩어리(동시에 녹을때까지)될때까지 반복
while True:
    # count값을 count_ice에서 받아온다
    count = count_ice()

    # count 2이상이면 년도 출력후 종료
    if count >= 2:
        print(year)
        break
    
    # count가 0이면 0출력후 종료
    if count == 0:
        print(0)
        break
    
    # 녹이는걸 한번할떄마다 년도 추가
    melt()
    year += 1