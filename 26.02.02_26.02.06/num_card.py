T = int(input())

for tc in range(1, T+1):
    cards = int(input())
    count_numbers = [0] * 10
    card_num = list(map(int, input().strip()))

    for _ in range(len(card_num)): # card_num리스트를 순회하면서
        count_numbers[card_num[_]] += 1 # card_num의 값을 numbers에 할당

    max_card_num = last_index = 0

    for x in range(len(count_numbers)):
        if count_numbers[x] >= max_card_num:
            max_card_num = count_numbers[x]

    last_index = max(last for last, nums in enumerate(count_numbers) if max_card_num==nums)

    print(f'#{tc} {last_index} {max_card_num}')
