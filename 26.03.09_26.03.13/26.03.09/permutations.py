def perm(length):
    case = 0

    if length==M:
        return 1
    
    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            pick_numbers.append(numbers[i])
            case+=perm(length+1)
            pick_numbers.pop()
            visited[i]=False
    return case


numbers = [1,2,3,4,5]
N = len(numbers)
M = int(input())
visited = [False]*N

pick_numbers = []

answer = perm(0)
print(answer)