import math

def left_right(length, left, right):
    global answer


    if left<right:
        return

    last_sum = 0
    sum_gaechu = 0

    for i in gaechu_list:
        sum_gaechu+=i
    last_sum = sum_gaechu-left-right
    if left>right+last_sum:
        answer+=(2**(N-length))*math.factorial(N-length)
        return

    if length==N:
        answer+=1
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            left_right(length+1, left+gaechu_list[i], right)
            left_right(length+1, left, right+gaechu_list[i])
            visited[i]=False
    
    return



T = int(input())

for tc in range(1,T+1):
    answer = 0
    N = int(input())
    gaechu_list = list(map(int, input().split()))
    visited = [False] * N
    left_right(0,0,0)

    
    print(f'#{tc} {answer}')