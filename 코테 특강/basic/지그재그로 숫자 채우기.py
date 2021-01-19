n, m = map(int, input().split())
arr = [[] for _ in range(n)]

cnt = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j].append(cnt)
            cnt += 1
    if i % 2 == 1:
        for k in range(n-1, -1, -1):
            arr[k].append(cnt)
            cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print("")