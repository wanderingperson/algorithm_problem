T = int(input())

for tc in range(1,T+1):
    pasckal = int(input())

    pasckal_triangle=[]
    for line in range(pasckal): # 0~pasckal-1번째줄
        pasckal_row=[1]*(line+1) # pasckal_row를 1로 미리 할당, 1번째줄은 1 1개, 2번째줄은 1 2개, 3번째줄은 .....
        for i in range(1, line): # line이 0, 1일때는 실행을 안함
            pasckal_row[i]=pasckal_triangle[line-1][i]+pasckal_triangle[line-1][i-1] # pasckal_row의 i번째값은 이전 줄 pasckal_row(즉, pasckal_triangle[line-1])의 현재값과 이전값을 더한다
        pasckal_triangle.append(pasckal_row) # pasckal_row의 값을 pasckal_triangle에 추가한다(paskcal_row가 리스트라서 리스트형태로 추가)


    print(f'#{tc}')
    for row in pasckal_triangle:
        print(*row)