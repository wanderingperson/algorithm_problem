N = int(input())

dr = [0,0,1,-1]
dc = [1,-1,0,0]


town_count=0
town_length_list = []

def DFS(r, c):
    global town_length
    town_length+=1
    visited[r][c]=1
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if (0<=nr<N) and (0<=nc<N) and (visited[nr][nc]!=1) and (square[nr][nc]==1):
            DFS(nr, nc)
    return 
        

square = [[] for _ in range(N)]
for i in range(N):
    square[i]=list(map(int, input()))

visited = [[0]*N for _ in range(N)]


for r in range(len(square)):
    for c in range(len(square[r])):
        if (square[r][c]==1) and (visited[r][c]!=1):
            town_length=0
            town_count+=1
            DFS(r, c)
            town_length_list.append(town_length)

town_length_list.sort()
print(town_count)
for row in town_length_list:
    print(row)
