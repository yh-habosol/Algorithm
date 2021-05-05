str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

DP = [[0]*m for _ in range(n)]

DP[0][0] = 1 if str1[0]==str2[0] else 0
for i in range(1,m):
    if str1[0] == str2[i]:
        DP[0][i] = 1
    else:
        DP[0][i] = DP[0][i-1]
for i in range(1,n):
    if str1[i] == str2[0]:
        DP[i][0] = 1
    else:
        DP[i][0] = DP[i-1][0]

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j])
print(DP[n-1][m-1])