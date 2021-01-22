DP = [1,1]

n = int(input())

for i in range(2, n):
    DP.append(DP[i-1] + DP[i-2])
print(DP[-1])