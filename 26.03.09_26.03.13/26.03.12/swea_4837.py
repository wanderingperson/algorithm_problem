number_list = [1,2,3,4,5,6,7,8,9,10,11,12]

T = int(input())

def comb(index,count, hab):
    global gajitsu

    if hab>K:
        return

    if index==12:
        if count==N and hab==K:
            gajitsu+=1
            return
        return


    comb(index+1,count+1, hab+number_list[index])
    comb(index+1,count,hab)

for tc in range(1,T+1):
    N, K = map(int, input().split())
    visited = [0]*12

    gajitsu = 0
    comb(0,0,0)
    print(f'#{tc} {gajitsu}')
