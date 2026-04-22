T = int(input())

for tc in range(1,T+1):
    day, month_1, month_3, year = map(int, input().split())
    year_plan = list(map(int, input().split()))
    dp = [0]*12 # 해당월까지의 누적합
    
    dp[0] = min(day*year_plan[0], month_1)
    for i in range(1,12):
        dp[i] = dp[i-1]+min(day*year_plan[i], month_1)

        if i>=2:
            dp[i] = min(dp[i], dp[i-3]+month_3)
    
    answer = min(dp[11],year)

    print(f'#{tc} {answer}')