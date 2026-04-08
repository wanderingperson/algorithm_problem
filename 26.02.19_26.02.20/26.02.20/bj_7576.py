from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs(q):
    count = 0

    while q:
        # 현재 depth 만큼만 큐에서 제거
        # 현재는 count 일차를 꺼내는 중입니다
        for _ in range(len(q)):
            current_r, current_c = q.popleft()

            for i in range(4):
                nr = current_r+dr[i]
                nc = current_c+dc[i]
                
                # 범위밖이면 건너뛰기
                if nr<0 or nr>=N or nc<0 or nc>=M:
                    continue

                # 해당 위치가 -1이면 건너뛰기
                if store[nr][nc]==-1:
                    continue
                
                # 해당 위치가 0이라면 1로 바꾸고 q에 추가
                if store[nr][nc]==0:
                    store[nr][nc]=1
                    q.append((nr,nc))
        count += 1

    return count

M, N = map(int, input().split())

result = 0
store = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()

for r in range(N):
    for c in range(M):
        if store[r][c]==1 and visited[r][c]==0:
            # 바로 bfs를 안하고 q에 추가하는 이유는 창고안에 익은토마토가 1개라는 법이 없기떄문
            q.append((r,c))
            visited[r][c]=1

result = bfs(q)

# 만약 아직 0인곳이있다면 -1을 출력하고 0인곳이 없다면 소요시간을 출력
for r in range(N):
    for c in range(M):
        if store[r][c]==0:
            print(-1)
            exit()
            
print(result-1)