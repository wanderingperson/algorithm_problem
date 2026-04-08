from itertools import combinations

for a in range(1,r):
    for group in combinations(range(r),a):
        groupA = set(group)
        groupB = set(range(r))-groupA
