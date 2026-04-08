T = int(input())

# K : 한번의 충전으로 지나칠 수 있는 정류장의 갯수
# N : 정류장의 총 길이
# M : 충전소의 갯수

# counts : 충전소 들린 횟수


for tc in range(1, T+1): #한번의 테스트케이스마다
    K,N,M = map(int,input().split()) #K, N, M을 받는다
    # N_list = [0] * (N+1) # N의길이 +1 만큼 배열생성(시작점포함)
    # N_list[0] = 1
    charge_stage = list(map(int, input().split())) # M의 값을 리스트에 할당
    # for charge in charge_stage: # 리스트 순회하면서
    #     N_list[charge] = 1 # N_list의 값에 배열 할당

# N_list[0]에서 시작
# K만큼 이동
# N_list[1~k]중에서 1인값이 없으면 counts = 0, 있으면 counts+=1, 위치저장
# 해당위치에서 K만큼 이동했을때 1인값이 없으면 counts = 0, 있으면 counts+=1, 위치저장
    counts = 0 # counts = 충전횟수
    position = 0 # position = 현재 위치

    # next_charge = 다음 충전
    # max_reach = 최대로 갈수 있는 거리

    while position + K < N: # position + K의 값이 정류장의 총 길이를 지나기 전까지 반복
        next_charge = position # next_charge에 position의 위치를 기록
        max_reach = position + K # max_reach에 position + K의 값을 기록
        for charge_list in charge_stage: # charge_stage의 리스트값을 순회
            if position < charge_list <= max_reach: # 현재위치와 현재위치에서부터 최대로 갈수있는 거리 사이에 charge_list의 값이 있다면
                next_charge = charge_list # next_charge에 charge_list의 값(즉 현재 정류장위치)을 넣음

        if next_charge == position: # 충전을 못해서 next_charge의 값이 position과 같다면
            counts = 0 # counts를 0으로 설정
            break
        
        position = next_charge # position에 next_charge값을 넣음
        counts += 1 # counts의 값을 1증가
        
    # for _ in range(len(charge_stage)):
    #     if position <= int(charge_stage[_+1]) <= (position+K): # 만약 다음정류장까지 한번에 갈 수 있다면
    #         _ += 1
    #     elif position <= int(charge_stage[_]) <= (position+K):
    #         counts += 1
    #         position = charge_stage[_]
    #     else:
    #         counts=0

    print(f'#{tc} {counts}')
