# 현재 뽑고있는 행
def n_queen(r):
    global answer

    if r == N:
        answer+=1  
        return
    
    for c in range(N):

        if c in visited: # 해당 열의 좌표가 이미 방문된 상태라면
            continue # 건너뛴다

        for test_r in range(r): # 현재 행(r)보다 위의 행들과 겹치는지 확인하기위함
            if r-test_r == abs(c-visited[test_r]):   # r은 test_r보다 무조건 크기떄문에(range(r)) r쪽은 abs를 씌울필요X
                break # 하나라도 대각선쪽에 위치하면 굳이 더 살펴볼필요가 없으므로 break

        else:
            visited[r] = c # 방문으로 표시
            n_queen[r+1]
            visited[r] = -1 # 원복시키기 위함





T = int(input())

# 방향을 잡아놓자


for tc in range(1,T+1):
    N = int(input())
    answer = 0

    # 방문안한 상태(-1) > 해당 행에 대해서 뽑지 않았다
    visited = [-1] * (N)

    # 0번부터 뽑기 시작
    n_queen(0)

    print(f'#{tc} {answer}')