N = int(input())

li = []
for i in range(N):
    name, score = input().split()
    li.append((name, int(score)))
li.sort(key = lambda x: x[1])
for i in li:
    print(i[0], end = ' ')