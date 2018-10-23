num = int(input())

for i in range(num):
    nA = int(input())
    a = set(map(int, input().split()))
    nB = int(input())
    b = set(map(int, input().split()))
    
    if not a.difference(b):
        print("True")
    else:
        print("False")