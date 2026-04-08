answer = float('inf')

def comb(start, selected):
    #전역변수 설정
    global answer
    
    # M개를 전부 골랐다면
    if len(selected) == M:
        # 거리를 0으로 초기화
        city_distance = 0

        # 집의 r,c좌표를 순회
        for hr, hc in house:

            #대소비교를 위해 가장 최댓값으로 설정
            min_distance = float('inf')

            #치킨집의 r,c좌표를 순회
            for cr, cc in selected:
                
                #r좌표 차이와 c좌표차이의 절대값
                distance = abs(hr - cr) + abs(hc - cc)

                #대소비교를 해서 min_distance에 추가
                min_distance = min(min_distance, distance)
                #여기서 집에서 가장 가까운 치킨집과의 거리를 얻게된다

            #city_distance에 치킨집의 최소거리들을 추가
            city_distance += min_distance
            
        answer = min(answer, city_distance)
        return

    # 치킨집의 위치를 selected에 추가 -> 조합
    for i in range(start, len(chicken)):
        selected.append(chicken[i])
        # 다음 인덱스부터 comb 실행
        comb(i+1, selected)
        # 원복시키기
        selected.pop()

# N, M입력받음
N,M = map(int, input().split())

# street 입력받음
street = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

#집의 위치와 치킨의 위치를 표기
for r in range(N):
    for c in range(N):
        if street[r][c] == 1:
            house.append((r, c))
        elif street[r][c] == 2:
            chicken.append((r, c))

#comb 실행
comb(0, [])

#answer출력
print(answer)