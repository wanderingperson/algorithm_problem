T = int(input())

for tc in range(1,T+1):

    num_input = int(input())

    num_list = list(map(int, input().split()))
    
    

    def SelectSort(arr,length): # 선택정렬
        for i in range(length-1): # 정렬구간의 시작 인덱스
            minimum_index = i # 시작인덱스를 최솟값으로 설정
            for j in range(i+1, length): # 인덱스 이후부터 length의값중에
                if arr[minimum_index] > arr[j]: # 시작인덱스에 있는 값보다 작은게 있다면
                    minimum_index = j 
            arr[minimum_index], arr[i] = arr[i], arr[minimum_index]
                
        return arr

    SelectSort(num_list, len(num_list))

    print(f'#{tc}', end=' ')
    
    for i in range(len(num_list)):
        print(num_list[i], end=' ')
    print()