T = int(input())

# 단, month는 실제 월 -1
def dfs(month, fee):
    global answer

    if fee >= answer:
        return
    
    if month >= 12: # 3달권으로 초과가 될수도 있어서 ==이 아닌 >=
        if answer > fee:
            answer = fee
        return
    
    
    # 현재 달에서 이동할수 있는 경우의 수

    # 일권
    dfs(month+1, fee + day_fee*days[month]) # 다음달로 넘어감, 이번달 비용(일일이용권)과 함께

    # 월권
    dfs(month+1, fee + month_fee) # 다음달로 넘어감, 이번달 비용(1달이용권)과 함께

    # 3개월권
    dfs(month+3, fee + quarter_fee) # 3달뒤로 넘어감, 3달치비용(3달이용권)과 함꼐
    

for tc in range(1,T+1):    
    day_fee, month_fee, quarter_fee, answer = map(int, input().split()) # 일일, 1달, 3달, 1년치 가격을 입력받음

    days = list(map(int, input().split())) # 각 달마다 수영장들리는 횟수 리스트로 입력받음

    dfs(0, 0) # 0(1월), 0(누적요금)

    print(f'#{tc} {answer}')