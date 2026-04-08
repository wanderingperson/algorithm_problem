# dfs 함수
def dfs(s):
    print(s, end=' ') # 현재 위치를 출력하고
    
    # 현재위치를 방문한곳으로 변경
    visited[s] = 1

    # 현재 노드에서 인접한 노드들을 확인한다
    for next_node in adj_node[s]:

        # 만약 인접한노드가 방문한 상태라면
        if visited[next_node]:
            continue
        # 해야 하는 일이 많아지면...
        dfs(next_node)
        

        # 만약 인접한노드가 미방문한 상태라면
        # if visited[next_node] == 0:
        #     dfs(next_node)

# N, M, V를 입력받음
N, M, V = map(int, input().split())

#이어져있는 노드 설정
adj_node = [[] for _ in range(N+1)]

# 노드가 1부터 시작하다보니까 N+1까지 설정
visited = [0]*(N+1)


# 양방향 노드 설정
for _ in range(M):
    a, b = map(int, input().split())
    adj_node[a].append(b)
    adj_node[b].append(a)

# 정점이 여러개일 경우 정점번호가 작은것을 먼저 방분
for i in range(len(adj_node)):
    adj_node[i].sort()


# V부터 방문
dfs(V)