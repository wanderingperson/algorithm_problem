T = int(input())

for tc in range(1, T+1):
    farm_length = int(input())

    farm = [[]*farm_length for _ in range(farm_length)]

    for _ in range(farm_length):
        farm[_] = list(map(int, input()))

    growth = 0

    mid = farm_length//2 # 7*7기준 3
    

    for r in range(len(farm)):
        c_start = abs(mid-r) #0,3 1,2 2,1 3,0 4,1 5,2 6,3
        c_end = farm_length-c_start-1 #0,3 1,4 2,5 3,6 4,5 5,4 6,3
        for c in range(c_start, c_end+1):
            growth+=farm[r][c]

    print(f'#{tc} {growth}')