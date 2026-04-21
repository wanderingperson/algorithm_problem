def guard_range(r,c,a,house_cost):
    global N
    a_cost = a**2 + (a-1)**2
    cost = 0
    house_count=0
    # a를 기준으로 i의 합이 a-1 이하
    for dr in range(-(a-1),a):
        column = (a-1) - abs(dr)
        for dc in range(-column, column+1):
            nr = r+dr
            nc = c+dc

            if 0<=nr<N and 0<=nc<N:
                if city[nr][nc]:
                    cost+=house_cost
                    house_count+=1
    
    if cost>=a_cost:
        return house_count
    return 0

def guard_cost(a, house_cost):
    answer = 0
    for r in range(N):
        for c in range(N):
            answer = max(answer,guard_range(r,c,a,house_cost))
    return answer


T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    max_house = 0

    city = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N+3,-1,-1):
        answer = guard_cost(i,M)
        if answer>max_house:
            max_house=answer
            break

    print(f'#{tc} {max_house}')