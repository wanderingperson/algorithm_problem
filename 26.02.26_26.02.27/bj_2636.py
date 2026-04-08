from collections import deque
import pprint


dr = [1,-1,0,0]
dc = [0,0,1,-1]

# 외부공기중 하나를 bfs에 넣는다? 외부공기하고 이어져있는걸 방문처리? (하나의 덩어리화)
# 현재 치즈들의 갯수를 센다. 이후 방문처리된 공기와 인접해있는 치즈들을 0으로 바꿔버린다. count+=1
# 위의 현재치즈갯수->0바꾸기를 반복하기
# 인접치즈가 현재치즈갯수와 같아지면 그게 녹기한시간전(2번째답)
# 이후의 count+=1이 1번째 답


# 녹을때

def melt():
    visited = [[0]*C for _ in range(R)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    melt_list = []

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0<=nr<R) and (0<=nc<C):
                if plate[nr][nc]==0 and not visited[nr][nc]:
                    visited[nr][nc]=1
                    q.append((nr,nc))

                elif plate[nr][nc]==1:
                    melt_list.append((nr,nc))
        
    for r, c in melt_list:
        plate[r][c]=0
    return len(melt_list)

# R, C입력
R, C = map(int, input().split())

# plate 입력
plate = [list(map(int, input().split())) for _ in range(R)]
time=0
last_count=0
# 다 녹을때까지 반복
while True:    
    count = 0
    for r in range(R):
        for c in range(C):
            if plate[r][c]==1:
                count+=1
    if count==0:
        print(time)
        print(last_count)
        break

    last_count=count
    melt()
    time+=1


