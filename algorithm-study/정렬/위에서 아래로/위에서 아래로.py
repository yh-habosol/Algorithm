N = int(input())
li = []
for i in range(N):
    n = int(input())
    li.append(n)
li.sort(reversed = True)

print(*li)
