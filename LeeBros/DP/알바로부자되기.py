n = int(input())
alba = []
for i in range(n):
    s, e, p = map(int, input().split())
    alba.append((s,e,p))
DP = [0]*n
DP[0] = alba[0][2]

for i in range(1, n):
    DP[i] = alba[i][2]
    for j in range(i-1, -1, -1):
        if alba[i][0] > alba[j][1]:
            DP[i] = max(DP[i], DP[j] + alba[i][2])
            
print(max(DP))