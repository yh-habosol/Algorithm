N = int(input())
room = list(map(int, input().split()))

DP = [room[0], max(room[0],room[1])]
for i in range(2, N):
	number = max(DP[i-2] + room[i], DP[i-1])
	DP.append(number)
print(DP[-1])