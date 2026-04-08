'''
N*N 크기 격자판이 있다
격자의 각 칸에는 정수가 하나씩 적혀 있다.
공은 어떤 칸에서 시작해서 상하좌우로 이동할 수 있다.
단, 이동할 수 있는 조건은 현재 칸보다 숫자가 작은 칸으로만 이동 가능하다.
(그중 값이 가장 작은곳으로 간다)
이동할 때마다 공은 한 칸씩 이동하며, 이동할 수 있을 때까지 계속 이동한다.
가장 많이 이동할 수 있는 경우의 이동 횟수를 구하는 문제다.
(출발칸을 포함해서 '이동한 칸의 수'를 센다)

'''

'''
Input
3
5
19 57 74 73 94
26 27 32 98 61
40 88 49 38 25
21 66 53 95 46
80 23 58 39 89
7
40 49 56 83 84 31 11
42 95 12 16 21 19 26
98 93 29 68 10 92 82
23 13 24 58 35 25 47
17 66 39 67 70 14 87
22 34 46 94 69 96 89
62 88 50 51 61 71 86
9
90 57 65 18 25 93 64 11 54
95 19 80 37 63 44 15 14 10
89 59 46 70 38 36 21 51 97
53 47 60 88 40 48 79 56 55
83 13 27 86 45 71 75 28 84
30 20 29 35 99 98 61 94 23
85 42 43 22 16 77 31 78 34
74 26 73 92 50 72 87 49 32
68 24 91 12 17 82 69 67 81
'''

'''
Output
6
10
9
'''

T = int(input())

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(r, c):
    global count
    count+=1
    min_index = 99
    for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]
        if (0<=next_r<N) and (0<=next_c<N):
            if square[r][c]>square[next_r][next_c]:
                if min_index>=square[next_r][next_c]:
                    min_index=square[next_r][next_c]
            
    
    
    for i in range(4):
        nnext_r = r+dr[i]
        nnext_c = c+dc[i]
        if (0<=nnext_r<N) and (0<=nnext_c<N):
            if min_index == square[nnext_r][nnext_c]:
                DFS(nnext_r, nnext_c)
    else:
        return

    


for tc in range(1,T+1):
    N = int(input())
    max_move = 0
    square = [list(map(int, input().split())) for _ in range(N)]

    for r in range(len(square)):
        for c in range(len(square)):
            count=0
            DFS(r,c)
            max_move = max(max_move, count)

    print(max_move)

