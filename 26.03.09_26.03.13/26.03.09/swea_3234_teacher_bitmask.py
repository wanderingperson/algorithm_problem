def dfs(count, visited, left, right):

    if count == N:
        return 1
    
    if dp[visited].get(left):
        return dp[visited][left]

    temp = 0
    for i in range(N):
        if visited & (1<<i):
            continue
        
        temp += dfs(count+1, visited|(1<<i), left+weights[i], right)
        if left>= right+weights[i]:
            temp += dfs(count+1, visited|(1<<i), left, right+weights[i])

    # 현재 visited상태에서 left무게일 떄의 경우의수를 반환
    dp[visited][left]=temp
    return dp[visited][left]

T = int(input())

for tc in range(1,T+1):
    N=int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**N)]  

    print(f'#{tc} {dfs(0,0,0,0)}')