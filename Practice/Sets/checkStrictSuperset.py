a = set(map(int, input().split()))
n = int(input())
output = True

for i in range(n):
    subset = set(map(int, input().split()))
    if a.difference(subset) and not subset.difference(a):
        output &= True
    else:
        output &= False
        
print(output)