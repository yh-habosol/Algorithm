n = int(input())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)
DP = [[0]*n for _ in range(n)]

DP[0][0] = grid[0][0]
for i in range(1,n):
    DP[0][i] = DP[0][i-1] + grid[0][i]
for i in range(1, n):
    DP[i][0] = DP[i-1][0] + grid[i][0]
    
for i in range(1, n):
    for j in range(1, n):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + grid[i][j]
print(DP[n-1][n-1])