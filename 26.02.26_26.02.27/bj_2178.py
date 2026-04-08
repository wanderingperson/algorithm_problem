from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(r,c):
    visited[r][c]=1

    q = deque()
    q.append((r,c))
    # time_count=0

    while q:
        r,c = q.popleft()

        # if (r==R-1) and (c==C-1):
            # print(time_count-1)
            # return


        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if (0<=nr<R) and (0<=nc<C):
                if miro[nr][nc]==1 and visited[nr][nc]==0:
                    visited[nr][nc] = 1 + visited[r][c]

                    q.append((nr,nc))
                    # time_count+=1





R, C = map(int, input().split())

miro = [list(map(int, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
BFS(0,0)

print(visited[R-1][C-1])



