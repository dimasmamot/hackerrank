M = input()
MList = set(map(int, input().split()))
N = input()
NList = set(map(int, input().split()))
    
for i in sorted(MList.symmetric_difference(NList)):
    print(i)