T = int(input())

dr = [0,1,0,-1] # 행의 값 변경하기 위한 dr
dc = [1,0,-1,0] # 열의 값 변경하기 위한 dc


for tc in range(1, T+1): 
    N = int(input())
    snail_number = [[0]*N for _ in range(N)]

    # 달팽이는 초반N칸이동, 이후 N-1칸이동*2, 이후 N-2칸이동*2...
    counts = [N]
    for i in range(N-1, 0, -1):
        counts.append(i)
        counts.append(i)

    r = c = 0
    dir = 0
    number = 1
    # count > 현재 방향으로 찍어줄 횟수가 적혀있음
    for count in counts:

        # count 만큼 이동하면서 숫자를 찍기
        for _ in range(count):
            # 1. 숫자 찍기
            snail_number[r][c] = number

            number += 1

            # 2. 이동
            r += dr[dir]
            c += dc[dir]
        
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir+1) % 4
        r += dr[dir]
        c += dc[dir]


    
    print(f'#{tc}')
    for row in snail_number:
        print(*row)