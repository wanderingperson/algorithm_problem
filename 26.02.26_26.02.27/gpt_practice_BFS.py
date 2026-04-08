from collections import deque


dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(r,c):
    distance = 0
    q = deque()
    q.append((r,c))
    visited[r][c]=1
    
    while q:
        r,c = q.popleft()

        if r==er and c==ec:
            return visited[r][c]-1

        
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if (0<=nr<R) and (0<=nc<C):
                if reach[nr][nc]==0 and visited[nr][nc]==0:
                    visited[nr][nc]=visited[r][c]+1
                    q.append((nr,nc))

    return -1




R, C = map(int, input().split())

reach = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]


sr, sc = map(int, input().split())
er, ec = map(int, input().split())
print(BFS(sr,sc))
