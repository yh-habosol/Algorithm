N = int(input())

DP = [1, 1, 2, 5]
for i in range(4, N+1):
    cn = 0
    for n in range(0, i):
        cn += (DP[n]*DP[i-1-n])
    DP.append(cn)
print(DP[N])