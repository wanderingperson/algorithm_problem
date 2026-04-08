T = 10


for tc in range(1,T+1):

    input()

    ladder = [list(map(int, input().split()))for _ in range(100)] # ladder를 통한 배열 할당
    r = 99
    c = ladder[99].index(2) # r이 99인곳에서 값이 2인 인덱스를 구한다
    dir = 0 #방향 세팅

    while r>0: #처음행(r=0)인 곳에 도달하기전까지 반복

        # 1. 왼쪽이 뚫려있으면
        # 왼쪽을 봤더니 1이 있다(단, 범위검사를 먼저 한다)
        while c-1 >= 0 and ladder[r][c-1]: # c-1 이 인덱스를 안벗어나고, ladder[r][c-1]이 1일시(1은 True처리라 생략가능)
            c -= 1 # c의값을 1 감소 
            dir = 1 # 방향값을 변경
        if dir == 1:
            r -= 1 # r의값을 1감소
            dir = 0 # 방향 초기화
            continue # 다시 처음부터 검사해라
        

        # 2. 오른쪽이 뚫려있으면
        while c+1 < 100 and ladder[r][c+1]: # c+1 이 인덱스를 안벗어나고, ladder[r][c+1]이 1일시(1은 True처리라 생략가능)
            c += 1 # c의값을 1 증가 
            dir = 2 # 방향값을 변경
        if dir == 2:
            r -= 1 # r의값을 1감소
            dir = 0 # 방향 초기화
            continue # 다시 처음부터 검사해라
        
        # 3. 좌우가 막혀있으면          

        r -= 1 # 위의 2개는 continue를 통해서 반복을 하기때문에 조건문없이 바로 작성 가능


    print(f'#{tc} {c}')