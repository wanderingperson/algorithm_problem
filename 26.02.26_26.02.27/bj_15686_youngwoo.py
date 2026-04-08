N , M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

answer = float('inf')

from itertools import combinations
for comb in combinations(chickens, M):
    city_distance = 0
    for hr, hc in houses:
        min_distance = float('inf')
        for cr,cc in comb:
            distance = abs(hr - cr) + abs(hc - cc)
            min_distance = min(min_distance, distance)
        city_distance += min_distance
    answer = min(answer, city_distance)
print(answer)
