T = int(input())

for tc in range(1,T+1):
    N = int(input())

    start_end = [list(map(int, input().split())) for _ in range(N)]
    count=0
    for r in range(N):
        for c in range(N):
            if start_end[r][0]>start_end[c][0] and start_end[r][1]<start_end[c][1]:
                count+=1
            elif start_end[r][0]<start_end[c][0] and start_end[r][1]>start_end[c][1]:
                count+=1
    print(f'#{tc} {count}')