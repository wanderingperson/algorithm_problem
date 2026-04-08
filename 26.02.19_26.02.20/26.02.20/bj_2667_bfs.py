dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(r,c):
    global town
    town+=1
    visited[r][c]=1

    for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]

        if (0<=next_r<N) and (0<=next_c<N) and square[next_r][next_c]==1:
            if visited[next_r][next_c]==0:
                DFS(next_r,next_c)
    return town

result = []


N = int(input())
square = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if square[r][c]==1 and visited[r][c]==0:
            town = 0
            result.append(DFS(r,c))

result.sort()
print(len(result))
for row in result:
    print(row)