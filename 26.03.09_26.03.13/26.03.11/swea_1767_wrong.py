import pprint

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def connect_line(r,c,N,processor):
    answer = N
    ex_line=[]
    for dir in range(4): # 델타 설정
        line_change = []
        nr = r
        nc = c
        K = 1 # 전선의 길이를 위한 설정
        while nr!=0 and nr!=N-1 and nc!=0 and nc!=N-1:
            nr = r+dr[dir]*K
            nc = c+dc[dir]*K
            if 0<=nr<N and 0<=nc<N:
                if processor[nr][nc]==1 or processor[nr][nc]==2:
                    break
                line_change.append((nr,nc))
                K+=1
        else:
            if answer>K:
                answer = K
                for ar, ac in ex_line:
                    processor[ar][ac]=0

                for xr,xc in line_change:
                    processor[xr][xc]=2
                ex_line = line_change.copy()
    if answer == N:
        return -1
    return answer

# 지금 문제점이 최대connect비교를 못하고있어
# 재귀느낌으로 가야하나?

def electric_line(N, processor):
    max_connect = 0
    min_connected_line = float('inf')
    connected_core = 0
    connected_line = 0

    for r in range(N):
        for c in range(N):
            if processor[r][c]==1:
                if r==0 or r==N-1 or c==0 or c==N-1: # 이미 붙어있는얘들을 미리 센다
                    connected_core+=1
                else:
                    if connect_line(r,c,N,processor)==-1:
                        continue
                    connected_line+=connect_line(r,c,N,processor) # 안붙어있으면 실행
                    connected_core+=1
    
    if connected_core > max_connect:
        if min_connected_line>connected_line:
            min_connected_line = connected_line
    
    return connected_line


T = int(input())

for tc in range(1,T+1):
    answer = 0
    N = int(input())

    processor = [list(map(int, input().split())) for _ in range(N)]
    answer = electric_line(N, processor)

    print(f'#{tc} {answer}')

    # r이 0이거나 N-1 # c가 0이거나 N-1
    # while r==0 or r==n-1 or c==0 or c==n-1: ?
    # nr = r+dr[i]*K
    # nc = c+dc[i]*K
    # K+=1?

    # dr, dc를 이용해서 최소길이가 나왔으면 connect유무를 설정하고 다음 코어쪽 재귀
    # 만약 경로에 1이나 2(전선)가 있다면 해당경로는 skip

    

    # 연결된 코어가 최대일때 갱신, 코어값이 같을 시 전선이 최소길이일때 갱신
    # 원복 코드
    # 답을 return 받는다

