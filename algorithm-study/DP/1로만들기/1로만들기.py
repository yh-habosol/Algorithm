X = int(input())
DP = [None, 0,1,1,2,1]
for i in range(6, X+1):
	a = DP[i//2] if i%2==0 else float('inf')
	b = DP[i//3] if i%3==0 else float('inf')
	c = DP[i//5] if i%5==0 else float('inf')
	
	n = min(DP[i-1]+1, a+1, b+1, c+1)
	DP.append(n)
print(DP[X])