T = int(input())

num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
num_dict = {} # 글자->숫자로 바꾸기위한 딕셔너리
num=0


for i in num_list: # num_list안에 있는 값들을 순회
    num_dict[i]=num # 해당 값들을 딕셔너리에 키로넣고, 밸류값으로는 해당 글자가 나타내는 숫자를 넣음
    num+=1 # 숫자+1

rev_dict = {} # 숫자->글자로 바꾸기위한 딕셔너리
for i in range(10): # 0~9까지
    rev_dict[i]=num_list[i] # 0~9를 키로넣고, 밸류값으로는 해당숫자가 나타내는 글자를 넣음
# print(num_dict.get('ONE'))

for tc in range(1, T+1):
    test_num, num_length = map(str, input().split()) # 테스트케이스번호와, 입력할 숫자의갯수 입력받음
    num_length = int(num_length) # 해당숫자만큼 반복문돌릴거라서 int로 벼환
    num_lists = list(map(str, input().split())) 
    
    for i in range(len(num_lists)): # num_lists의 갯수만큼 반복문 돌림
        num_lists[i]=(num_dict.get(num_lists[i])) # 해당 인덱스에 있는값(글자)를 숫자로 변경

    num_lists.sort() # 정렬하기
    
    new_num=[]
    for i in num_lists: # 정렬한 num_list를 순회하면서
        new_num.append(rev_dict[i]) # 해당숫자에 알맞는 글자로 new_num에 추가
    
    print(test_num)
    for i in range(len(new_num)):
        print(new_num[i], end=' ')
