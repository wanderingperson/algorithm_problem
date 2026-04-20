from collections import deque
import copy

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(cnt, bricks): # 현재 쏜 구슬의 갯수, 현재 벽돌 상태 / 각 가지 수마다 실행했을 때를 저장하기 위해 
    global answer
    if cnt == N:
        total_brick = cnt_brick(bricks)
        answer = min(answer, total_brick)
        return
    
    for c in range(W):
        _bricks = copy.deepcopy(bricks)

        shoot(c, _bricks)
        dfs(cnt+1, _bricks)


def bfs(r, c, bricks): # 블럭 터지는 걸 q에서 한꺼번에 처리하기 위해
    q = deque()
    q.append((r, c, bricks[r][c])) # 현재 좌표와 블럭의 크기를 q에 저장

    while q:  # q에 값이 남아있지 않을 때까지 
        r, c, power = q.popleft()
        bricks[r][c] = 0
        for d in range(4):
            for k in range(power):
                nr = r + dr[d]*k
                nc = c + dc[d]*k

                if 0 <= nr < H and 0 <= nc < W and bricks[nr][nc]:
                    q.append((nr, nc, bricks[nr][nc]))
    return

    

def shoot(c, bricks):  # 각 c 좌표마다 맨 위에 있는 값을 찾는다 / 구슬을 발사하는 함수
    for r in range(H):
        if bricks[r][c]:
            bfs(r, c, bricks)
            gravity(bricks)
            break


def gravity(bricks):  # 벽돌 깬 후 위치 갱신
    for c in range(W):
        stack = []
        for r in range(H):
            if bricks[r][c]:
                stack.append(bricks[r][c])

        for r in range(H-1, -1, -1):
            if stack:
                bricks[r][c] = stack.pop()
            else:
                bricks[r][c] = 0
                

def cnt_brick(bricks):  # 마지막에 남아있는 블럭 갯수 세기
    cnt = 0
    for r in range(H):
        for c in range(W):
            if bricks[r][c] >= 1:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    answer = float('inf')
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    dfs(0, bricks)
    print(f'#{tc} {answer}')