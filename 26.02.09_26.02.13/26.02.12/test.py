# numbers = [1,2,3]
# pick_idx = [0]*len(numbers)


# # def subset(count):

# #     # 다 골랐을 때
# #     if count == len(numbers):
# #         for i in range(len(pick_idx)):
# #             if pick_idx[i]:
# #                 print(numbers[i], end = ' ')
# #         print()

# #         return

# #     # 아직 안 골랐을 때
# #     pick_idx[count] = 0 # 현재 자리의 값을 안고른다
# #     subset(count+1)

# #     pick_idx[count] = 1 # 현재 자리의 값을 고른다
# #     subset(count+1)

# # subset(0)

numbers = [1,2,3]
pick_numbers = []

def comb(count, idx):
    # 모든 조합의 수를 출력
    print(pick_numbers)
    if count ==3:
        # 길이3일때만 출력
        # print(pick_numbers)
        return

    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
    # 조합
    comb(count+1, i+1)

    # 중복 조합
    # comb(count+1, i)

    pick_numbers.pop()

comb(0,0)