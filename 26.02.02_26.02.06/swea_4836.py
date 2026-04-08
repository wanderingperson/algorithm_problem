T = int(input())

for tc in range(1,T+1):
    tyle = [[0]*10 for _ in range(10)]

    coloring = int(input())
    

    for color in range(coloring):
        r1,c1,r2,c2,colors = map(int, input().split())

        # 색깔이 color일 때
        # 이미 나의 색깔이 칠해진 경우
        # 이미 나의 색깔이 아닌 색이 칠해진 경우
        # 이미 둘 다 칠해진 경우 
        # # 아무것도 칠해지지 않은 경우
        # for r in range(r1, r2+1):
        #     for c in range(c1, c2+1):
        #         # 이미 둘 다 칠해졌거나 자기 색깔이 칠해진 경우 > 건너뜀
        #         if tyle[r][c] == colors or tyle[r][c] == 3:
        #             continue
        #         # 내 색깔이 아닌 색이 칠해진 경우 > 덧칠
        #         elif (colors == 1 and tyle[r][c] == 2) or (colors == 2 and tyle[r][c] == 1):
        #             tyle[r][c] = 3
        #         # 비어있을 때 > 나의 색깔로 색칠
        #         elif tyle[r][c] == 0:
        #             tyle[r][c] = colors

                    
                

        if colors==1:
            for r in range(r1,r2+1):
                for c in range(c1, c2+1): 
                    if(tyle[r][c]==2):
                        tyle[r][c]=3
                    elif(tyle[r][c]!=3):
                        tyle[r][c]=1
        elif colors==2:
            for r in range(r1,r2+1):
                for c in range(c1, c2+1):
                    if(tyle[r][c]==1):
                        tyle[r][c]=3
                    elif(tyle[r][c]!=3):
                        tyle[r][c]=2

    count = 0

    for r in range(10):
        for c in range(10):
            if tyle[r][c]==3:
                count+=1
    
    print(f'#{tc} {count}')

