def dfs(cutting):
    global min_cut

    conflict = False

    for i in range(N):
        for j in range(i+1, N):

            s1,e1 = start_end[i]
            s2,e2 = start_end[j]

            if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
                conflict = True

                se = start_end[i]
                start_end[i] = [0,0]

                dfs(cutting+1)

                start_end[i] = se

    if not conflict:
        min_cut = min(min_cut, cutting)
    


N = int(input())

start_end = [list(map(int, input().split())) for _ in range(N)]
start_end.sort()
min_cut = N

dfs(0)

print(min_cut)
# dfs식으로 해볼까


