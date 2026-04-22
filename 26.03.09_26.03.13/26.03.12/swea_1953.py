from collections import deque

T = int(input())

# dr,dc로 생각하자
# 1:상하좌우, 2:상하, 3:좌우, 4:상우, 5:하우, 6:하좌, 7:상좌
pipe_number = {
    1 : [[-1,1,0,0],[0,0,-1,1]],
    2 : [[-1,1,0,0],[0,0,0,0]],
    3 : [[0,0,0,0],[0,0,-1,1]],
    4 : [[-1,0,0,0],[0,0,0,1]],
    5 : [[0,1,0,0],[0,0,0,1]],
    6 : [[0,1,0,0],[0,0,-1,0]],
    7 : [[-1,0,0,0],[0,0,-1,0]]
}

# 현재 파이프가 이전것과 연결되어있는지 확인하기
def connected(r,c,nr,nc,pipe_num):
    if pipe_num!=0:
        for i in range(4):
            origin_r = nr + pipe_number[pipe_num][0][i]
            origin_c = nc + pipe_number[pipe_num][1][i]

            if origin_r==r and origin_c==c:
                return True
    return False


def move_available(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c]=1
    length=1
    time_count=1

    while q:
        # time_count가 L일때 길이 반환
        if time_count==L:
            return length
        
        # 같은시간대에 있는건 한번에 처리하자
        for _ in range(len(q)):
            cr,cc = q.popleft()

            # 파이프안에 있으니까 무조건 1이상의 값이 나온다
            pipe_num = pipe_list[cr][cc]
            for i in range(4):
                # 가상의 nr, nc
                nr = cr+pipe_number[pipe_num][0][i]
                nc = cc+pipe_number[pipe_num][1][i]

                # 범위 안일때
                if (0<=nr<N) and (0<=nc<M):
                    # 파이프가 있고 미방문상태라면
                    if pipe_list[nr][nc]!=0 and visited[nr][nc]==0:
                        # 가상위치파이프가 현재거하고 연결되어있다면
                        if connected(cr,cc,nr,nc,pipe_list[nr][nc]):
                            q.append((nr,nc))
                            visited[nr][nc]=1
                            length+=1
        time_count+=1

    return length





    # 일단 현재 위치를 이동가능리스트에 넣자
    # if visited[r][c]==0:
    #     # 일단 방문체크를 하자
    #     visited[r][c]=1

    #     # 만약 경과시간이 L과 같다면 종료하자
    #     if time_count==L:
    #         return move_list
        
    #     # 이전것과 연결되어있는지 확인하고 연결되어있다면 진행
    #     move_list.append((r,c))
    #     for i in range(4):
    #         nr = r + pipe_number[pipe_num][0][i]
    #         nc = c + pipe_number[pipe_num][1][i]
    #         if 0<=nr<N and 0<=nc<M:
    #             if connected(r,c,nr,nc,pipe_list[nr][nc]):
    #                 if pipe_list[nr][nc]!=0:
    #                     move_available(time_count+1,nr,nc,pipe_list[nr][nc])
    # else:
    #     return


for tc in range(1,T+1):
    # N : 세로, M : 가로, R : 뚜껑세로위치, C : 뚜껑가로위치, L : 걸린시간
    N,M,R,C,L = map(int, input().split())

    pipe_list = [list(map(int, input().split())) for _ in range(N)]
    move_list=[]
    visited = [[0]*M for _ in range(N)]

    answer = move_available(R,C)


    print(f'#{tc} {answer}')
    # 거기에 있는 숫자를 생각하자
    
    # 시간이 지날때마다 가능한 리스트들을 append해서
    # len(리스트)를 하면 되지않을까?
    # 안이어져있는것도 세버리는게 문제네?