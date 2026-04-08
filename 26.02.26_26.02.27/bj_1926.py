from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c):
    global picture_length
    q = deque()
    visited[r][c]=1
    q.append((r,c))
    picture_current_length = 0

    while q:
        cr, cc = q.popleft()
        picture_current_length+=1
        

        for i in range(4):
            nr = cr+dr[i]
            nc = cc+dc[i]

            if (0<=nr<R) and (0<=nc<C):
                if picture_list[nr][nc]==1 and visited[nr][nc]==0:
                    visited[nr][nc]=1
                    q.append((nr,nc))
    picture_length = max(picture_length, picture_current_length)

R, C = map(int, input().split())

picture_list = [list(map(int, input().split()))for _ in range(R)]
visited = [[0]*C for _ in range(R)]
picture_count=0
picture_length = 0

for r in range(R):
    for c in range(C):
        if picture_list[r][c]==1 and visited[r][c]==0:
            bfs(r,c)
            picture_count+=1

print(picture_count)
print(picture_length)
