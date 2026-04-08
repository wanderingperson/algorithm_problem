def dfs(node): # 현재 방문하고 있는 노드를 매개변수, dfs에 관한 정의
    
    global answer # answer는 전역변수라서 global설정
    visited[node] = 1 # 현재 노드를 일단 방문한곳으로 저장

    if node == 99 or answer: # 만약 목적지에 도달한 상태거나, answer이 1인경우(다른루트에서 99를 찾았을 경우)
        answer = 1 # answer를 1로 변경 후 종료
        return

    for next_node in adj_list[node]: 

        # next_node가 방문한 상태일시 건너뜀
        if visited[next_node] == 1:
            continue

        # next_node가 미방문 상태일시 dfs(next_node)를 실행
        dfs(next_node)
    
    else:

T = 10

for tc in range(1,T+1):
    answer = 0 # 초기 가능/불가능 여부는 불가능으로 남겨놓음
    adj_list = {}
    _, M = map(int, input().split()) # 테스트케이스 번호와 간선의 총 갯수


    # info의 길이 = M * 2
    info = list(map(int,input().split())) # 노드와 노드끼리 이어져있는 것들을 입력한다

    for i in range(0, M*2, 2): # road의 갯수만큼 순회
        a, b = info[i], info[i+1] # node_to_node의 시작점과 도착점을
        adj_list[a] = adj_list.get(a, []) # adj_list[a]에 넣는다. 만약 a키에 대한 밸류값이 없는 상태라면 빈 리스트로 생성
        adj_list[a].append(b) # 넣는다. 이때 일방통행이라서 adj_node[b].append(a)는 할필요 없음

    visited = [0]*100 # 미방문지역을 0으로 설정
    dfs(0) 


    answer = dfs(0)

    print(f'#{tc} {answer}') # #테스트케이스번호, 가능/불가능여부


