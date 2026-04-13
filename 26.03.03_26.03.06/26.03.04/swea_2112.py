from itertools import combinations
import copy

# D : 보호필름의 두께
# W : 보호필름의 가로길이
# K : 합격기준(같은 가로인덱스, 연속된 K열이 같아야함)
# T : 테스트케이스 갯수
# 0 : A, 1 : B
T = int(input())

# 성능검사 테스트 함수
def test(film):
    # 성능검사 통과 확인
    # 연속된 세로막의 값을 확인하기 위한 변수
    okay_film=0
    # i 과 j를 이용해서 연속된곳이 있는지 확인해볼까
    # i : 세로인덱스, j : 가로인덱스
    # j는 끝까지 순회를 하자
    for j in range(W):

        # 초기 film_count는 1
        film_count = 1
        # 초기0번째열,j번째행의 값을 status에 저장
        status = film[0][j]
        # i는 1~D까지 순회를 하자
        for i in range(1,D):
            # status와 값이 같다면
            if film[i][j]==status:
                # film_count 1증가
                film_count+=1
            # k번만큼 반복하고 그값이 K-1과 같다면
            else: # 만약 값이 다르다면
                film_count=1 # film_count를 초기화하고 status도 현재 위치의 값으로 갱신
                status = film[i][j]
            # 만약 film_count와 K의값이 같다면 테스트 통과이므로 break
            if film_count==K:
                break
        else: # break문을 안만났다면 테슽 불합격이므로 False반환
            return False
    return True

# dfs함수에 관한 정의
def dfs(idx):
    # 만약 변환한 idx가 change와 같다면 test함수실행후 값 반환
    if idx == change:
        return test(film)
    
    # 바꿔야할 인덱스의 값을 row에 할당
    row = comb[idx]

    # row번째 인덱스에 A 넣기
    film[row] = filmA
    if dfs(idx+1):
        return True
    # row번째 인덱스에 B 넣기
    film[row] = filmB
    if dfs(idx+1):
        return True

    # 테스트통과가 안됐다면 원상복구
    film[row] = film_spare[row]
    return False


for tc in range(1,T+1):
    # answer : 결과값
    answer = 0

    D, W, K = map(int, input().split())

    # 약품A와 B를 투입했을때의 막 생성
    filmA = [0]*W
    filmB = [1]*W

    film = [[]*W for _ in range(D)]

    # 현재 필름의 배열들을 할당
    for i in range(D):
        film[i] = list(map(int, input().split()))
    film_spare = copy.deepcopy(film)

    # 만약 test를 바로 통과 못하면
    if not test(film):
        
        # K 이내로 못하면 답은 K이므로 K까지만 돌리기
        for change in range(1, K):
            find_answer = False
            # 전체막에서 change할 막을 조합으로 구하기
            for comb in combinations(range(D), change):
                
                # dfs(0)이 실행완료(테스트통과)됐으면
                if dfs(0):
                    # 정답유무를 True로 변환
                    find_answer = True
                    # answer에 change할당 후 break
                    answer = change
                    break
            # 정답유무가 True일시 break(for-else를 건너뛰기위함)
            if find_answer:
                break
        # 정답유무가 False일시(break미발동)
        else:
            # K가 정답이므로 answer에 K할당
            answer = K
    # 지금 해야할건
    # 조합을 통해서
    # 약품A, B를 기존 막과 교체하고 성능검사 테스트를 하는것
    # 

    print(f'#{tc} {answer}')