def DFS(s): #시작점을 매개변수, DFS에 관한 정의
    global answer
    visited[s] = 1

    if s == 99:
        answer = 1
        return
    
    for next_node in adj_list[s]:

        if visited[next_node]:
            continue

        DFS(next_node)

T = 10

for tc in range(1,T+1):
    answer = 0 # 초기 가능/불가능 여부는 불가능으로 남겨놓음
    adj_list = [[] for _ in range(100)] # 인접 리스트는 0~99까지의 값을 가질 수 있다.
    _, M = map(int, input().split()) # 테스트케이스 번호와 간선의 총 갯수
    visited = [0]*100

    # info의 길이 = M * 2
    info = list(map(int,input().split())) # 노드와 노드끼리 이어져있는 것들을 입력한다

    for i in range(0, M*2, 2): # road의 갯수만큼 순회
        a, b = info[i], info[i+1] # node_to_node의 시작점과 도착점을
        adj_list[a].append(b) # 넣는다. 이때 일방통행이라서 adj_node[b].append(a)는 할필요 없음
    
    DFS(0)

    print(f'#{tc} {answer}') # #테스트케이스번호, 가능/불가능여부


