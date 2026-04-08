T = 10

for tc in range(1,T+1):
    answer = 0 # 초기 가능/불가능 여부는 불가능으로 남겨놓음
    adj_list = [[] for _ in range(100)] # 인접 리스트는 0~99까지의 값을 가질 수 있다.
    _, M = map(int, input().split()) # 테스트케이스 번호와 간선의 총 갯수


    # info의 길이 = M * 2
    info = list(map(int,input().split())) # 노드와 노드끼리 이어져있는 것들을 입력한다

    for i in range(0, M*2, 2): # road의 갯수만큼 순회
        a, b = info[i], info[i+1] # info의 시작점과 도착점을
        adj_list[a].append(b) # 넣는다. 이때 일방통행이라서 adj_node[b].append(a)는 할필요 없음


    def DFS(s): #시작점을 매개변수, DFS에 관한 정의
        visited = [0] * (100) # 미방문한지역을 전부 0으로 표기
        stack = [s] # 스택은 일단 빈공간

        while stack: # 참인동안 계속 반복

            # 현재 지점 방문 처리
            if visited[s] == 0: # s번인덱스가 미방문상태일시
                visited[s] = 1 # s번 인덱스를 방문상태로 변경

                # 단, 현 지점이 도착지라면 중단
                if s==99: # s의 값이 99일시
                    return 1 # 1을 반환
            
            # 다음 지점 찾기
            for w in adj_list[s]: # 인접리스트에 있는 값들을 순회

                # 다음 지점 중 갈 수 있는 곳이 있다면 순회 중단
                if visited[w]==0: # 인접리스트에 있는 값이 미방문 상태일 시
                    stack.append(s) # 스택에 현재 인덱스좌표값을 저장
                    s=w # 인접리스트에 있는값을 현재 좌표에 대입
                    break # 반복문을 끝낸다
            
            # 현 지점에서 할 일이 없다는 뜻 > stack에서 제거 필요
            else: # 만약 인접리스트에 있는 값이 없을 시 (막다른 길)
                if stack: # 스택에 값이 있다면
                    s = stack.pop() # pop을 한값을 s에 대입한다
                else: # 스택에 값이 없다면
                    break # 반복문을 끝낸다
        return 0 # While문이 끝날때까지 99와 이어진 노드가 없었다면 0 반환

    answer = DFS(0)

    print(f'#{tc} {answer}') # #테스트케이스번호, 가능/불가능여부


