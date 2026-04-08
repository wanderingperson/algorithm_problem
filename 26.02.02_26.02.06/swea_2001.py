T = int(input())

for tc in range(1, T+1):
    result = 0 # 결과값
    
    n,c= map(int, input().split()) # n=타일의 크기(n*n), c=파리채의 크기(c*c)
    
    arr = [list(map(int, input().split())) for _ in range(n)]

    for garo in range(n-c+1): # 인덱스오류가 나지않기위해 파리채 시작좌표설정
        for saero in range(n-c+1):  
            killcount = 0 # 잡은 파리 수

            for fly in range(c): 
                for kill in range(c):

                    killcount+=arr[garo+fly][saero+kill] # 파리채의 넓이안에 있는값들을 전부 더함

            result = max(result, killcount) # result와 killcount비교해서 더큰값으로 갱신

    print(f'#{tc} {result}')