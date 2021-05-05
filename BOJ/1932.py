n = int(input())

tree = []

for i in range(n):
    temp = list(map(int, input().split()))
    tree.append(temp)

DP = [[0]*n for _ in range(n)]
DP[0][0] = tree[0][0]
for i in range(1, n):
    DP[i][0] = tree[i][0] + DP[i-1][0]
    DP[i][i] = tree[i][-1] + DP[i-1][i-1]
count = 1
for i in range(2, n):
    for j in range(i-count, i):
        DP[i][j] = max(DP[i-1][j-1] + tree[i][j], DP[i-1][j] + tree[i][j])
    count += 1

print(max(DP[-1]))
