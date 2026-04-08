T = int(input())

def dfs(row):
    global count

    # 모든 행에 퀸을 놓았으면 성공
    if row == N:
        count += 1
        return

    for col in range(N):

        # 현재 위치에 둘 수 있는지 확인
        possible = True

        for prev_row in range(row):
            # 같은 열이거나 대각선이면 불가능
            if (board[prev_row] == col) or (abs(prev_row - row) == abs(board[prev_row] - col)):
                possible = False
                break

        if possible:
            board[row] = col
            dfs(row + 1)

for tc in range(1, T+1):
    N = int(input())
    count = 0
    board = [-1] * N   # board[row] = col 의미

    dfs(0)

    print(f'#{tc} {count}')