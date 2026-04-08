T = int(input())


#각 줄마다 첫값과 끝값은 연산을 할 필요가 없다
#가운데에 있는 값일때 연산을 실행
for tc in range(1,T+1):
    N = int(input())
    before_row =[] # 처음 before_row는 빈 리스트

    print(f'#{tc}')
    # i : 지금 몇 번째 줄인가
    for i in range(1,N+1):
        current_row = [] # current_row값은 다음줄로 넘어갈때마다 초기화
        for j in range(i):
            if j == 0 or j == i-1: # j(열 인덱스)가 첫값(0)이거나 끝값(i-1)일때
                current_row.append(1) # current_row에 1의값을 추가한다
                print(1, end=' ') # 1을 출력
                
            else: # 가운데에 있는 값이면
                current_row.append(before_row[j]+before_row[j-1]) # 이전 줄의 현재인덱스의 값과 현재인덱스-1의 값을 더해서 추가한다
                print(before_row[j]+before_row[j-1], end= ' ')
        print()
        before_row = current_row # 반복문이 끝나면 current_row는 before_row의값에 넣는다