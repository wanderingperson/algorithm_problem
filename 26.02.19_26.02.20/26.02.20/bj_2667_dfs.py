from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r, c):
    q  = deque()
    
    # 각 단지의 길이는 town?
    town = 1
    q.append((r,c))
    visited[r][c]=1

    while q:
        current_r, current_c = q.popleft()
        for i in range(4):
            nr = current_r+dr[i]
            nc = current_c+dc[i]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if square[nr][nc]==0 or visited[nr][nc]==1:
                continue
            visited[nr][nc]=1
            q.append((nr,nc))
            town+=1

    return town



N = int(input())
square = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

result = []
for r in range(N):
    for c in range(N):
        if square[r][c] and visited[r][c]==0:
            result.append(bfs(r,c))
result.sort()

print(len(result))
for row in result:
    print(row)