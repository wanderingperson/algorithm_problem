dr = [-1,1,0,0]
dc = [0,0,-1,1]

def make_seven(r,c,number):

    if len(number)==7:
        differt_seven_length.add(number)
        return

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if 0<=nr<4 and 0<=nc<4:
            make_seven(nr,nc,number+str(number_list[nr][nc]))

T = int(input())

for tc in range(1,T+1):
    
    number_list = [list(map(int, input().split())) for _ in range(4)]

    differt_seven_length = set()

    for r in range(4):
        for c in range(4):
            make_seven(r,c,str(number_list[r][c]))

    print(f'#{tc} {len(differt_seven_length)}')