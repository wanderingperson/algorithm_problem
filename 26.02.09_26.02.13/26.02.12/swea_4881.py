T = int(input())

# r번째 행에 관한 DFS
def DFS(r, today_sum):
    global min_sum


    # 만약 현재까지의 합이 최솟값을 넘었다면 스킵
    if today_sum>=min_sum:
        return
    
    # 현재 행이 N과 같다면 최솟값을 갱신
    if r == N:
        min_sum = today_sum
        return min_sum

    
    for column_i in range(N):    
        if visited[column_i]: # 만약 이미 사용한 열이라면..
            continue
        else: # 사용하지 않은 열이라면..
            visited[column_i]=1
            today_sum+=square[r][column_i]
            DFS(r+1, today_sum)
            today_sum-=square[r][column_i]
            visited[column_i]=0
    
    return today_sum

    
    # 백트래킹

for tc in range(1,T+1):
    min_sum = float('inf')
    N = int(input())
    
    square = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N)


    today_sum = 0
    DFS(0, today_sum)

    print(f'#{tc} {min_sum}')

