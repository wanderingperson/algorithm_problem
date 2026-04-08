T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minimum = arr[0]
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] <= minimum:
            minimum = arr[i]
        if arr[i] >= maximum:
            maximum = arr[i]
    print(f'#{tc} {maximum-minimum}')
