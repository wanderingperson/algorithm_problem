T = 10

    # dump_try = 덤프 시도 횟수
    # box_length = 박스의 높이
    # max_length = 최대높이를 가진 box
    # min_length = 최소높이를 가진 box

    # 한번의 dump_try마다, box_length의 리스트에서 max_length를 가진 값과, min_length를 가진 값을 알아내고
    # max_length - 1, min_length + 1을 해서 box_length에 해당 값을 반영
    # 끝나고 나면 max_length와 min_length의 차이값을 출력

for tc in range(1, T+1):
    dump_try = int(input())
    box_length = list(map(int, input().split()))

    for _ in range(dump_try): # 한번의 dump_try마다

        max_length = min_length = box_length[0]
        maxs = mins = 0

        for i in range(len(box_length)): # box_length 전체를 순회해서

            if box_length[i] >= max_length: # 최댓값과 최솟값을 구한다
                maxs = i
                max_length = box_length[i]
            if box_length[i] <= min_length:
                mins = i
                min_length = box_length[i]

        if max_length - min_length <= 1:
            break

        box_length[maxs] -= 1
        box_length[mins] += 1


    print(f'#{tc} {max(box_length)-min(box_length)}')