# 부분문제의 해결방안을 전체문제에 적용시켜서 해결 가능하다면 greedy를 적용

T = int(input())

for tc in range(1,T+1):
    # 나무 갯수
    N = int(input())

    # 각 나무의 높이
    heights = list(map(int, input().split()))

    max_height = max(heights)
    #가장 적게 쓴 날짜
    answer = 0

    one_count = 0
    two_count = 0
    for height in heights:

        if height == max_height:
            continue
        
        one_count+=(max_height-height)%2
        two_count+=(max_height-height)//2

    while two_count - one_count > 1:
        two_count-=1
        one_count+=2

    if one_count > two_count:
        answer = 2*one_count-1
    else:
        answer = 2*two_count
    
    print(f'#{tc} {answer}')
    