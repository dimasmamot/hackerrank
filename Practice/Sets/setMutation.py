nA = input()
a = set(map(int, input().split()))
c = int(input())

for i in range(c):
    cmd = (input().split())[0]
    cmdSet = set(map(int, input().split()))
    if cmd == 'intersection_update':
        a.intersection_update(cmdSet)
    elif cmd == 'update':
        a.update(cmdSet)
    elif cmd == 'symmetric_difference_update':
        a.symmetric_difference_update(cmdSet)
    elif cmd == 'difference_update':
        a.difference_update(cmdSet)

print(sum(a))