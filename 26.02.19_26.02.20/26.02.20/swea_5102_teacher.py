from collections import deque

# 거리를 return한다
def bfs(S):
    q = deque()
    visited = [0]*(V+1)

    q.append(S)
    visited[S]=1

    distance = 0

    while q:
        # 현재 큐에 있는만큼만 pop == 현 step(층)에서 담긴 만큼만
        for _ in range(len(q)):
            node = q.popleft()
            if node == G:
                return distance

            # 현재 지점에서 연결된얘들을 탐색
            for next_node in adj_list[node]:
                # 이미 방문한 지점이면 건너뛴다
                if visited[next_node]:
                    continue
                visited[next_node]=1
                q.append(next_node)
        # pop을 다하면 거리를 1 증가시킨다
        distance += 1


T = int(input())





for tc in range(1,T+1):
    V,E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]  
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    S, G = map(int, input().split())
    
    print(f'#{tc} {bfs(S)}')