dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(r,c):
    global length
    visited[r][c]=1
    length+=1

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if (0<=nr<R) and (0<=nc<C):
            if reach[nr][nc]==0 and visited[nr][nc]==0:
                DFS(nr,nc)
    return length



R, C = map(int, input().split())

reach = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

length=0
sr, sc = map(int, input().split())
print(DFS(sr,sc))
