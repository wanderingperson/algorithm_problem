T = int(input())

def plant_tree(tree_list):
    answer = 0
    max_tree = tree_list[0]

    for i in range(1, len(tree_list)):
        if max_tree == tree_list[i]:
            continue
        elif (max_tree-tree_list[i]) % 2 == 0:
            even_plant(max_tree, tree_list[i])
        else:
            odd_plant(max_tree, tree_list[i])
    
    return answer

# 높이 차이가 짝수일때
def even_plant(max_tree, current_tree):
    global answer

    chai = max_tree-current_tree
    # 만약 차이가 딱2가 나는데
    if chai==2:
        # 만약 현재 날짜가 홀수라면
        if answer % 2 !=0:
            answer+=2
            return
        # 만약 현재 날짜가 짝수라면
        else:
            answer+=1
            return
    # 차이가 딱 2가 아니라면(높이차이는 짝수고정임)
    else:
        pass


def odd_plant(max_tree, current_tree):
    global answer

    chai = max_tree-current_tree
    # 만약 차이가 1이 딱 나는데
    if chai==1:
        # 만약 현재 날짜가 홀수라면
        if answer % 2 !=0:
            answer+=1
            return
        # 만약 현재 날짜가 짝수라면
        else:
            answer+=2
            return
    # 차이가 딱 1이 아니라면(높이차이는 홀수고정임)
    else:
        pass



for tc in range(1,T+1):
    N = int(input())
    tree_list = list(map(int, input().split()))
    max_tree = max(tree_list)
    need_plant = 0
    odd = 0
    even = 0

    for i in tree_list:
        chai=max_tree-i
        need_plant+=chai
        odd+=chai%2
        even+=chai//2
    
    # 홀수+1은 짝수, 우린 홀수날부터 시작
    while even>odd+1:
        even-=1
        odd+=2

    if odd>even:
        answer = odd*2-1
    else:
        answer = even*2

    print(f'#{tc} {answer}')


# 가장 큰 나무하고 현재 인덱스의 차이를 확인하자
# 현재날짜가 홀 / 짝일때
# 만약 차이가 1이라면 홀 / x 홀
# 만약 차이가 2라면 x 짝 / 짝
# 만약 차이가 3이면 홀 짝 / 짝 홀
# 만약 차이가 4라면 홀 짝 홀 / 짝 x 짝
# 만약 차이가 5라면 x 짝 홀 짝 / 짝 홀 짝
# 만약 차이가 6이라면 홀 짝 홀 짝 / 짝 홀 짝 홀
# 만약 차이가 7이라면 홀 짝 홀 짝 홀 / x 홀 짝 홀 짝 홀
# 만약 차이가 8이라면 x 짝 홀 짝 홀 짝 / 짝 홀 짝 홀 짝
# 만약 차이가 9라면 홀 짝 홀 짝 홀 짝 / 짝 홀 짝 홀 짝 홀
# 만약 차이가 10이라면 홀 짝 홀 짝 홀 짝 홀 / x 홀 짝 홀 짝 홀 짝 홀


# 재귀 느낌인가?
# 홀수에서
# 4=3+1, 5=2+3, 7=3+4, 9=6+3, 10=9+1=6+3+1

# 짝수에서
# 5=3+2, 6=3+3, 7=1+6, 10=3+7