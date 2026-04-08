T = int(input())

for tc in range(1,T+1):
    A, B = input().split()
    
    count = 0

    i = 0
    while i < (len(A)-len(B)+1):
        if A[i:i+len(B)]==B:
            count+=1
            i += len(B)
        else:
            i += 1

    result = len(A)-count*(len(B)-1)

    print(f'#{tc} {result}')


    # aaaassdd aa
    