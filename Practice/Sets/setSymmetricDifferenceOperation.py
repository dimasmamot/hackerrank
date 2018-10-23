nA = input()
a = set(map(int, input().split()))
nB = input()
b = set(map(int, input().split()))

print(len(a.symmetric_difference(b)))