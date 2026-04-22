dr = [-1,1,0,0]
dc = [0,0,1,-1]

def dfs(r,c,move_room,base_room):
    global max_move
    global start_room

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue

        if room_list[nr][nc]==room_list[r][c]+1:
            dfs(nr,nc,move_room+1, base_room)
            break
    else:
        if move_room<max_move:
            return
        
        if move_room>max_move:
            max_move = move_room
            start_room = base_room
        
        if move_room==max_move:
            start_room = min(start_room,base_room)


T = int(input())

for tc in range(1,T+1):
    N = int(input())

    room_list = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    start_room = N

    for r in range(N):
        for c in range(N):
            dfs(r,c,1,room_list[r][c])
    
    print(f'#{tc} {start_room} {max_move}')