dr = [1,-1,0,0]
dc = [0,0,1,-1]


# 지금 문제점이 최대connect비교를 못하고있어
# 재귀느낌으로 가야하나?

def electric_line(N, processor):
    core_list=[]

    for r in range(N):
        for c in range(N):
            if processor[r][c]==1:
                if r==0 or r==N-1 or c==0 or c==N-1: # 이미 붙어있는얘들을 미리 센다
                    continue
                else:
                    core_list.append((r,c))

    dfs(core_list,0,0,0)
    return min_line_length

def dfs(core_list,core_index, line_length, connected_core):
    global max_core
    global min_line_length
    if core_index == len(core_list):
        if max_core<connected_core:
            max_core=connected_core
            min_line_length=line_length
        elif max_core==connected_core:
            min_line_length=min(min_line_length, line_length)
        return min_line_length

    r,c = core_list[core_index]

    length=0

    for dir in range(4):

        path = []

        nr = r
        nc = c

        while True:
            nr += dr[dir]
            nc += dc[dir]

            if not (0<=nr<N and 0<=nc<N):
                break

            if processor[nr][nc] != 0:
                path = []
                break

            path.append((nr,nc))

        if path:
            for pr, pc in path:
                processor[pr][pc]=2
            dfs(core_list,core_index+1, line_length+len(path), connected_core+1)
            for pr, pc in path:
                processor[pr][pc]=0

    dfs(core_list,core_index+1, line_length, connected_core)


T = int(input())

for tc in range(1,T+1):
    answer = 0
    N = int(input())

    processor = [list(map(int, input().split())) for _ in range(N)]
    max_core = 0
    min_line_length = 0
    electric_line(N, processor)
    answer = min_line_length

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

