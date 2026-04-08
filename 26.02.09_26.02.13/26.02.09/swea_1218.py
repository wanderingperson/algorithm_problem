T = 10
for tc in range(1, T+1):
    length = int(input())
    top=-1

    arr=list(input())
    stack = [0]*length

    answer=0

    for i in arr:
        
        if top!=length-1:
            if i == '(':
                top+=1
                stack[top] = '('
            elif i == '{':
                top+=1
                stack[top] = '{'
            elif i == '[':
                top+=1
                stack[top] = '['
            elif i == '<':
                top+=1
                stack[top] = '<'

            elif i in ')}]>':
                if top==-1:
                    answer=0
                    break
                else:
                    top-=1
                    if stack[top+1]=='(' and i==')':
                        continue
                    elif stack[top+1]=='{' and i=='}':
                        continue
                    elif stack[top+1]=='[' and i==']':
                        continue
                    elif stack[top+1]=='<' and i=='>':
                        continue
                    else:
                        answer=0
                        break
    if top!=-1:
        answer=0
    else:
        answer=1
    
    print(f'#{tc} {answer}')