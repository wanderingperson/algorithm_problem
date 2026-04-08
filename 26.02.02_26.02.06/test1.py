arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# print(list(zip(arr[0],arr[1],arr[2]))) # 굳이 이렇게 안써도 됨

print(list(zip(*arr))) # 한번에 언패킹 하면됨