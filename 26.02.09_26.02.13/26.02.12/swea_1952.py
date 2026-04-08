T = int(input())


def DFS(month, price):
    global min_price

    if price>=min_price: # 만약 지금까지의 값이 최솟값(1년정액권)을 넘어버리면 바로 종료
        return

    if month>=len(year_plan): # 3달권으로 초과가 될수도 있어서 ==이 아닌 >=
        min_price = min(price, min_price) # 현재까지 구한 최솟값과 현재의 값을 비교해서 최솟값 갱신
        return
    
    
    DFS(month+1, price + day*year_plan[month]) # 다음달로 넘어감, 이번달 비용(일일이용권)과 함께

    DFS(month+1, price + month_1) # 다음달로 넘어감, 이번달 비용(1달이용권)과 함께

    DFS(month+3, price + month_3) # 3달뒤로 넘어감, 3달치비용(3달이용권)과 함꼐
    

for tc in range(1,T+1):    
    day, month_1, month_3, year = map(int, input().split()) # 일일, 1달, 3달, 1년치 가격을 입력받음
    min_price = year # 1년치이용권을 최솟값으로

    year_plan = list(map(int, input().split())) # 각 달마다 수영장들리는 횟수 리스트로 입력받음

    DFS(0, 0) # 0(1월), 0(현재까지 구한값)

    print(f'#{tc} {min_price}')