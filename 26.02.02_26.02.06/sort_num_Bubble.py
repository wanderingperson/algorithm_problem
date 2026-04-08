T = int(input())

for tc in range(1,T+1):

    num_input = int(input())

    num_list = list(map(int, input().split()))
    
    

    def BubbleSort(arr,length):
        for i in range(length-1, 0, -1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

        return arr

    BubbleSort(num_list, len(num_list))

    print(f'#{tc}', end=' ')
    
    for i in range(len(num_list)):
        print(num_list[i], end=' ')
    print()