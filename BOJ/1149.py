N = int(input())

RGB = []
for i in range(N):
    a, b, c = map(int, input().split())
    temp = [a, b, c]
    RGB.append(temp)

R = [RGB[0][0]]
G = [RGB[0][1]]
B = [RGB[0][2]]

for i in range(1, N):
    R.append(min(G[i-1] + RGB[i][0], B[i-1] + RGB[i][0]))
    G.append(min(R[i-1] + RGB[i][1], B[i-1] + RGB[i][1]))
    B.append(min(R[i-1] + RGB[i][2], G[i-1] + RGB[i][2]))
print(min(R[-1], G[-1], B[-1]))
