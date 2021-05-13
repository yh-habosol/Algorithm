N = int(input())

DP = [1, 3]
if N <= 2:
	print(DP[N-1]%796796)
else:
	for i in range(2, N):
		DP.append(DP[i-2]*2 + DP[i-1])
	print(DP[N-1]%796796)