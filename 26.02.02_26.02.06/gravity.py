TestCase = int(input())
for tc in range(1, TestCase+1):
    T = int(input())
    box = list(map(int, input().split()))
    comp = []

    for compare in range(len(box)-1):
        counts = 0
        for compare_list in range(compare+1, len(box)):
            if box[compare] > box[compare_list]:
                counts += 1
        comp.append(counts)

    max_comp = comp[0]
    for i in range(len(comp)):
        if comp[i] > max_comp:
            max_comp = comp[i]

    print(f'#{tc} {max_comp}')
