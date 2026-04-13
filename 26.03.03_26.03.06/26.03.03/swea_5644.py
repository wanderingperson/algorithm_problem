dr = [-1,0,1,0]
dc = [0,1,0,-1]

playerA = [0,0]
playerB = [9,9]

T = int(input())

for tc in range(1,T+1):
    M, A = map(int, input().split())
    playerA_move = list(map(int, input().split()))
    playerB_move = list(map(int, input().split()))

    ap_list = [[] for _ in range(A)]
    for i in range(A):
        ap_list[i]=list(map(int, input().split()))
    
    for x in ap_list: