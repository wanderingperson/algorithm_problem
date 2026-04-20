from itertools import permutations

def left_right(index,length):
    global answer
    global visited
    visited[index]=True

    if length==N:
        answer+=1

    for j in range(index+1,N):
        if not visited[j]:
            left_gaechu.append(perm[j])
            left_right(j, length+1)
            left_gaechu.pop()
            visited[j]=False

            
            if sum(left_gaechu)>=sum(right_gaechu)+perm[j]:
                right_gaechu.append(perm[j])
                left_right(j, length+1)
                right_gaechu.pop()
                visited[j]=False




T = int(input())

for tc in range(1,T+1):
    answer = 0
    N = int(input())
    gaechu_list = list(map(int, input().split()))

    gaechu_perm = permutations(gaechu_list)


    for perm in gaechu_perm: # 처음 왼쪽칸에 넣어놓을걸 생각중...
        left_gaechu = []
        right_gaechu = []
        visited = [False] * N

        for i in range(len(perm)):
            left_gaechu.append(perm[i])
            left_right(i,1)
    
    print(f'#{tc} {answer}')