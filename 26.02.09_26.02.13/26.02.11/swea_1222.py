T = 10

for tc in range(1,T+1):
    

    length = int(input())
    jungwi = list(input())
    huwi = []
    plus_stack = []

    for i in jungwi:
        if i == '+':
            if plus_stack:
                huwi.append(plus_stack.pop())
                plus_stack.append(i)
            else:
                plus_stack.append(i)

        else:
            huwi.append(i)
    while plus_stack:
        huwi.append(plus_stack.pop())

    gyesan = []
    for token in huwi:
        result = 0

        if token != '+':
            gyesan.append(int(token))
        else:
            op1 = gyesan.pop()
            op2 = gyesan.pop()

            result = op1+op2
            gyesan.append(result)
    
    answer = gyesan.pop()




    print(f'#{tc} {answer}')