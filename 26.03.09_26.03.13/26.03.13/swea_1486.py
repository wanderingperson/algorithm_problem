T = int(input())

def tower(index, sum_height):
    global minimum_difference
    if sum_height>=B:
        minimum_difference = min(minimum_difference, sum_height-B)
        return
    
    if index==N:
        return
    
    if sum_height-B>=minimum_difference:
        return

    tower(index+1, sum_height+height_list[index])
    tower(index+1, sum_height)
    
    return

for tc in range(1,T+1):
    N, B = map(int, input().split())

    height_list = list(map(int, input().split()))

    minimum_difference = sum(height_list)-B

    tower(0,0)
    print(f'#{tc} {minimum_difference}')
