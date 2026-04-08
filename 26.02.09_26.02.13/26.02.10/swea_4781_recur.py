T = int(input())

for tc in range(1,T+1):
    answer = 0
    # 노드의 갯수 V와 간선의 갯수 E를 입력받음
    V, E = map(int, input().split())

    # start_end 리스트를 선언하고 각 리스트마다 이어져있는 노드를 입력받음
    start_end = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        s, e = map(int, input().split())
        start_end[s].append(e) 


    # DFS에 관한 선언
    def DFS(start, end):

        # answer을 global로 설정(길이가 짧아서 사용, 다른경우엔 비권장)
        global answer

        # 현재 노드를 방문한곳으로 변경
        visited[start]=1

        # 만약 현재 노드가 목표노드와 같을 시
        if start == end:
            # answer을 1로 변경
            answer = 1
            return
            
        # 현재 노드에서 이어져있는 노드들을 순회
        for next_node in start_end[start]:

            # 만약 이어져있는 노드가 이미 방문한곳이라면 건너뜀
            if visited[next_node]:
                continue
            
            # 만약 이어져있는 노드가 방문하지 않은곳이라면(else처리나 마찬가지)
            DFS(next_node, end) # 재귀호출

    st, en = map(int, input().split())

    DFS(st, en)
    print(f'#{tc} {answer}')