T = int(input())

# K : 한번의 충전으로 지나칠 수 있는 정류장의 갯수
# N : 정류장의 총 길이
# M : 충전소의 갯수

# answer : 충전소 들린 횟수


for tc in range(1, T+1): #한번의 테스트케이스마다
    answer = 0
    K, N, M = map(int, input().split())
    bus_stops = [0] + list(map(int, input().split()))

    cur_pos = stop_idx = 0
    
    while cur_pos + K < N :

        for i in range(M, stop_idx, -1):
            if bus_stops[i] <= cur_pos + K:
                stop_idx = i
                cur_pos = bus_stops[i]
                answer +=1
                break

        # 다음 충전소를 못 찾았을 때
        else:
            answer = 0
            break




    print(f'#{tc} {answer}')
