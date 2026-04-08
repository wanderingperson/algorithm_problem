# 중위순회를 위한 함수
def inorder(node):
    # 탐색순서 : LVR

    # 왼쪽의 자식 노드를 먼저 확인한다. 단, 왼쪽의 자식노드가 있을때만
    if node*2<=N:
        inorder(node*2)
    
    # 자기 자신을 출력
    print(tree[node], end='')

    # 오른쪽의 자식 노드를 이후 확인.
    if node*2+1 <=N:
        inorder(node*2+1)

T = 10

for tc in range(1,T+1):

    #노드의 갯수
    N = int(input())
    tree = [0]*(N+1) # 0은 사용안할거라서 N+1까지
    for idx in range(1, N+1):
        # 두번째가 문자로 고정이라서 두번째만 가져옴
        info = input().split()
        tree[idx] = info[1]




    print(f'#{tc} ',end='')
    # 중위순회를 하면서 출력
    inorder(1)
    print()