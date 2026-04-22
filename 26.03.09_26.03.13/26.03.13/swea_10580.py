# 교차점 발생 규칙
# 새로운 선이
# 1. 기존의 선보다 시작점은 높고, 도착점은 낮다
# 2. 기존의 선보다 시작점은 낮고, 도착점은 높다
# 새로운 선이 들어오면, 기존의 모든 선들과 비교
# -> 완전 탐색
# - 시간복잡도 - O(N^2), 연산횟수 : 1+2+3+......+N-1(약 50만번) (N은최대1000)

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    wires = []
    answer = 0

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존의 모든 선들과 시작점, 도착점을 비교
        for prev_start, prev_end in wires:
            if start>prev_start and end<prev_end:
                answer+=1
            if start<prev_start and end>prev_end:
                answer+=1

        # 기존 목록에 start, end를 추가
        wires.append((start,end))
    
    print(f'#{tc} {answer}')