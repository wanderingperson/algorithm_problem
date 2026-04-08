from collections import deque

T = 10
for tc in range(1, T+1):
    _ = input()

    numbers = deque(map(int, input().split()))
    
    i=0
    minus_index=[1,2,3,4,5]
    while True:        
        a = numbers.popleft()

        if a-minus_index[i] <=0:
            a=0
            numbers.append(a)
            break
        else:
            a=a-minus_index[i]
            numbers.append(a)
            i = (i+1)%5



    print(f'#{tc}', end = ' ')
    for row in numbers:
        print(row, end = ' ')
    print()

