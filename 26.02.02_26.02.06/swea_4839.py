T = int(input())

for tc in range(1,T+1):
    result = 0

    P, A, B = map(int, input().split())

    def binary_search(pages,key):
        counts = 0
        start = 1
        end = pages
        while start <= end:
            counts+=1
            middle = (start+end)//2
            if middle == key:
                return counts
            elif middle > key:
                end = middle

            else:
                start = middle
       
        return counts
    
    A_count = binary_search(P, A)
    B_count = binary_search(P, B)
    if A_count == B_count:
        result = 0
    elif A_count > B_count:
        result = 'B'
    else:
        result = 'A'
            

    print(f'#{tc} {result}')