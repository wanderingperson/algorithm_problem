T = int(input())


for tc in range(1,T+1):
    N, K = map(int, input().split())

    length_count = 0

    square = [list(map(int, input().split())) for _ in range(N)]

    for r in range(len(square)):
        count = 0
        for c in range(len(square[r])):
            
            if square[r][c]==1:
                count+=1
            elif square[r][c]==0:
                if count==K:
                    length_count+=1
                count=0
            
            if count==K:
                length_count+=1

                        
            # 만약 r, c가 1이라면..
            # 해당 방향으로만 포문을 K만큼 돌리고
            # 현재좌표+K가 0이면 count를 +1한다..
    for c in range(len(square)):
        count = 0
        for r in range(len(square[r])):
            
            if square[r][c]==1:
                count+=1
            elif square[r][c]==0:
                if count==K:
                    length_count+=1
                count=0
            
            if count==K:
                length_count+=1

                        
            # 만약 r, c가 1이라면..
            # 해당 방향으로만 포문을 K만큼 돌리고
            # 현재좌표+K가 0이면 count를 +1한다..

    print(f'#{tc} {length_count}')