# charge_idxs > 2차원리스트 [[A가 충전할수 있는 위치 인덱스 모음], [B가 충전할수 있는 위치 인덱스 모음]]

# 1. 이동(M번)
    # 2. 이동한 위치에서 A,B 충전할 수 있는 충전소 파악
        # -1. A,B와 충전소 간의 거리 파악 > 해당 거리가 충전범위 이내이면 충전 가능
    # 3. 최적의 충전량 고르기 > max
        # -1.A만 충전할 수 없는 경우 (charge_idxs B만 반복문을 돌린다)
        # -2.B만 충전할 수 없는 경우 (charge_idxs A만 반복문을 돌린다)
        # -3.A,B 둘다 충전 가능한 경우 (charge_idxs A, B를 2중for문으로 돌린다)
    # 4. max 누적



# dr, dc 방향이동
# 0:정지 1:상, 2:우, 3:하, 4:좌
dr = [0,0,1,0,-1]
dc = [0,-1,0,1,0]

# T 테스트케이스의 갯수
T = int(input())

for tc in range(1,T+1):
    answer = 0
    
    # M 이동횟수
    # N 배터리의 수
    M , N = map(int, input().split())

    # A, B 각각 A/B의 이동 경로(델타의 인덱스)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # human_rcs A(0),B(1)의 좌표
    human_rcs = [[1,1],[10,10]]

    # BC_info 배터리의 정보(N개)
    # BC_info > N만큼 반복
    # 0, 1 > 좌표
    # 2 > 충전 범위
    # 3 > 충전량
    BC_info = [0]*N
    for i in range(N):
        BC_info[i] = list(map(int, input().split()))

    # 충전 > M+1
    for time in range(M+1):
        # 충전 가능한 위치 탐색 - A, B
        charge_idxs = [[],[]]
        # A, B중 누구를 돌지 (human rcs 0번인덱스, 1번인덱스)
        # i : A인지 B인지
        for i in range(2):
            r,c = human_rcs[i]
            # 어떤 충전소인지 선택
            # j : 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, chargo_amount = BC_info[j]
                
                # 거리가 충전 범위 이내라면
                if abs(r-BC_r)+abs(c-BC_c) <=coverage:
                    # 해당 충전 가능한 위치에 충전소 번호를 추가
                    charge_idxs[i].append(j)

        # 최적 충전량 - 3-1, 3-2, 3-3
        charge = 0
        # A가 충전할수 없는 경우
        if not charge_idxs[0]:
            # B가 충전가능한 충전소 번호들을 탐색해서
            for i in charge_idxs[1]:
                # charge보다 충전량이 크면 charge를 갱신
                if BC_info[i][3]>charge:
                    charge = BC_info[i][3]

        # B가 충전할수 없는 경우
        elif not charge_idxs[1]:
            for i in charge_idxs[0]:
                if BC_info[i][3]>charge:
                    charge = BC_info[i][3]
        # A,B 둘다 충전 가능한 경우
        else:
            # i : A의 충전소 번호
            for i in charge_idxs[0]:
                # j : B의 충전소 번호
                for j in charge_idxs[1]:
                    # 만약 i과 j가 같을때(충전량은 절반이 됨)
                    if i == j:
                        # 만약 BC_info[i][3]의 충전량이 지금까지의 충전량보다 크다면
                        if BC_info[i][3] > charge:
                            # 둘이 같은 충전소를 쓸때 충전량은 절반이라서 두개를 더하면 충전량 하나와 마찬가지
                            charge = BC_info[i][3]
                    else:
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]
        answer+=charge

        # 이동
        
        # 이동은 M-1번까지 하니까 M일때는 time에 남은 리스트가 없어서 오류가 나온다
        if time != M:
            # A의 r,c좌표
            human_rcs[0][0] += dr[A[time]]
            human_rcs[0][1] += dc[A[time]]

            # B의 r,c좌표
            human_rcs[1][0] += dr[B[time]]
            human_rcs[1][1] += dc[B[time]]


    print(f'#{tc} {answer}')