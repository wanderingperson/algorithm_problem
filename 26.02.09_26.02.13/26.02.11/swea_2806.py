T = int(input())

# 방향을 잡아놓자
dr = [0,0,1,-1,1,-1,1,-1] # 가로, 세로, 대각선순서
dc = [1,-1,0,0,1,1,-1,-1]

for tc in range(1,T+1):
    result = 0

    queen = int(input())
    queen_count=0

    chess_board = [[0]*queen for _ in range(queen)]



    # 퀸의 현재 위치와 퀸이 지나갈수있는 경로를 전부 1처리
    for r in range(queen):
        for c in range(queen):

            #만약 퀸의 현재 좌표가 다른퀸이 지나갈수가 없는 경로라면
            if queen[r][c]==0:
            # 갈수있는 경로를 전부 1처리하고 난 뒤에
                for i in range(8):
                    for j in range(queen):

                        # 만약 퀸의 현재좌표가 다른퀸이 지나갈수가 없는 경로라면
                        if queen[r][c]==0:
                            queen[r][c]=1
                            nr = r + dr[i] * j
                            nc = c + dc[i] * j

                            if (0<=nr<queen) and (0<=nc<queen):
                                queen[nr][nc]=1
                queen_count += 1
            
            else:
                break
    
    if queen_count == queen:
        result+=1

    print(chess_board)









    print(f'#{tc} {result}')