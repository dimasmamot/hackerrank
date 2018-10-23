n, room = int(input()), list(map(int, input().split()))
roomSet = set(room)

print(int(((sum(roomSet)*n) - (sum(room)))/(n-1)))
