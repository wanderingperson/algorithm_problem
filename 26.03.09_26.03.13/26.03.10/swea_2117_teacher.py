def calc_cost(K):
    return K**2 + (K-1)**2

def search_K(k, cost):
    max_home_count = 0

    for r in range(N):
        for c in range(N):
            home_count = 0
            for dr in range(-(K-1), K):
                for dc in range(-(K-1), K):

                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nr>=N or nc<0 or nr>=N:
                        continue
                    if abs(dr)+abs(dc)>=K:
                        continue
                    if graph[nr][nc]==0:
                        continue
                    home_count+=1
            if home_count>max_home_count and home_count*M >= cost:
                max_home_count = home_count
    



T = int(input())

for tc in range(1,T+1):
    answer = 1
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]

    max_K = N+1 if N % 2 == 0 else N

    for K in range(max_K, 1, -1):
        # K일 때, 커버할 수 있는 최대 집의 수를 return
        result = search_K(K, calc_cost(K))
        if result >= 1:
            answer = result
            break


    print(f'#{tc} {answer}')