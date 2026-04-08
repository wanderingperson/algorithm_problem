

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def DFS(row,column):
    global answer
    visited[row][column]=1

    for i in range(4):
        nr = row+dr[i]
        nc = column+dc[i]

        if (0<=nr<16) and (0<=nc<16):
            if square[nr][nc]==0 and visited[nr][nc]==0:
                DFS(nr,nc)
            elif square[nr][nc]==3:
                answer = 1
                return

for tc in range(1,11):
    _ = int(input())
    square = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    answer = 0
    for r in range(16):
        for c in range(16):
            if square[r][c]==2:
                DFS(r, c)

    print(f'#{tc} {answer}')