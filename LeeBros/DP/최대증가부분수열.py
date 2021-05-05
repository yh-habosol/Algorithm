N = int(input())
L = list(map(int, input().split()))

DP = [0]*N
DP[0] = 1

for i in range(1, N):
    DP[i] = 1
    for j in range(i-1, -1, -1):
        if L[i] > L[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))