T = int(input())


for tc in range(1,T+1):
    A_length, B_length = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    indx=0
    for a in A_list:
        if a==B_list[indx]:
            indx+=1
            if indx==B_length:
                break
        
    if indx==B_length:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')


# # 강사님 풀이
# T = int(input())

# for tc in range(1, T+1):
#     answer = 'NO'

#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     B_idx = 0

#     # YES인 상황
#     for number in A:
#         if B[B_idx] == number:
#             B_idx+=1
#             if B_idx >= M:
#                 break

#     if B_idx ==M:
#         answer = 'YES'

#     print(f'#{tc} {answer}')


# # 강사님 풀이2
# T = int(input())

# for tc in range(1, T+1):
#     answer = 'YES'

#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     for number in B:
#         if number not in A:
#             answer = 'NO'
#             break
        
#         idx = A.index(number) # index안에 이미 반복문이 있어서 시간복잡도로는 비효율적
#         A=A[idx+1:] # 슬라이싱으로 A에 재할당


#     print(f'#{tc} {answer}')