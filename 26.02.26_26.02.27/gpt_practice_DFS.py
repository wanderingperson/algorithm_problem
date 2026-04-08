dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(r,c):

    if reach[r][c]==3:
        return 1
    
    visited[r][c]=1
    count = 0

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if (0<=nr<R) and (0<=nc<C):
            if reach[nr][nc]==0 and visited[nr][nc]==0:
                count += DFS(nr,nc)
    visited[r][c]=0

    return count




R, C = map(int, input().split())

reach = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

solution=0
for sr in range(R):
    for sc in range(C):
        if reach[sr][sc]==2:
            print(DFS(sr,sc))