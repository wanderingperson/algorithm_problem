from itertools import combinations
from collections import deque

def connected(group):
    q=deque()
    visited = set()

    start = list(group)[0]
    q.append(start)
    visited.add(start)

    while q:
        current = q.popleft()
        for next_node in node_to_node[current]:
            if next_node in group and next_node not in visited:
                visited.add(next_node)
                q.append(next_node)
    return len(visited)==len(group)


N = int(input())
# 1부터 N까지가 아닌 0부터 N-1까지의 인구 수
population=list(map(int, input().split()))
node_to_node = [[] for _ in range(N)]


for j in range(len(population)):
    
    temporary = list(map(int, input().split()))
    for i in range(1,len(temporary)):
        node_to_node[j].append(temporary[i]-1)


answer = float('inf')

for r in range(1,N):
    for groupA in combinations(range(N),r):
        groupA=set(groupA)
        groupB=set(range(N))-groupA

        if connected(groupA) and connected(groupB):
            popA = sum(population[i] for i in groupA)
            popB = sum(population[i] for i in groupB)
            answer = min(answer, abs(popA-popB))


if answer == float('inf'):
    print(-1)
else:
    print(answer)
