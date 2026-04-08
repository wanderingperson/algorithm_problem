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
        stack = [start]
        visited[start] = 1

        # stack에 값이 있을동안 반복
        while stack:

            # start에 현재 stack의 마지막값을 넣는다
            start = stack[-1]
            
            # 만약 start의 값이 end와 같다면 1 반환
            if start == end:
                return 1
            
            # 인접 노드들을 순회
            for next_node in start_end[start]:

                # 만약 해당 인접 노드가 이미 방문한상태일시 스킵
                if visited[next_node]:
                    continue

                # 그게 아니라면 stack에 next_node를 추가한다
                stack.append(next_node)
                visited[next_node] = 1
                break

            # 인접 노드에서 더이상 갈곳이 없다면
            else:
                stack.pop()

            
        
        # 기본적으로 0 반환
        return 0
            
   

    start, end = map(int, input().split())

    
    print(f'#{tc} {DFS(start, end)}')