n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
hapiness = 0

for i in arr:
    if i in a:
        hapiness += 1
    elif i in b:
        hapiness -= 1

print(hapiness)