T = 10

for tc in range(1, T+1):
    length = int(input())
    puzzle = [input() for _ in range(8)]

    count = 0



    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])-length+1): # 해당 좌표들 안에서
                
            puzzle_list = []

            puzzle_list += puzzle[r][c:c+length]
            # 행쪽에서 회문 찾기
            if puzzle_list == puzzle_list[::-1]: # 가로회문찾기
                count+=1

    for r in range(len(puzzle)-length+1):           
        for c in range(len(puzzle[0])):

            puzzle_list = []

            for i in range(length):
                puzzle_list += puzzle[r+i][c]
            # puzzle_list += puzzle[r:r+length][c] 이건 왜 오류가
            
            if puzzle_list == puzzle_list[::-1]:
                count+=1


    print(f'#{tc} {count}')
