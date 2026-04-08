T = 10


for tc in range(1,T+1):

    testcase = int(input())

    ladder = [[0]*100 for _ in range(100)]

    for _ in range(100):
        zero_one = list(map(int, input().split()))

        ladder[_] = zero_one # ladder리스트에 값들 추가
    
    result = 0


    for start in range(100):


        #만약1이면
        r=99
        for c in range(100):
            if ladder[r][c]==2: # 만약 1이 아니라면
                break
    
        while r>0:

            if (c < 99) and ladder[r][c+1]==1:
                while (c < 99) and ladder[r][c+1]==1:
                    c+=1
                r-=1

            elif (c > 0) and ladder[r][c-1]==1:
                while (c > 0) and ladder[r][c-1]==1:
                    c-=1
                r-=1
            else:
                r-=1              



    print(f'#{testcase} {c}')