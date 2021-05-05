n = int(input())

DP = [None, 0, 1, 1]
a = None
b = None
c = None
for i in range(4, n+1):
    if i % 3 == 0:
        a = (DP[i // 3]+1)
    if i % 2 == 0:
        b = (DP[i // 2]+1)
    c = DP[i-1]+1

    if a and b:
        DP.append(min(a, b, c))
    elif a and not b:
        DP.append(min(a, c))
    elif not a and b:
        DP.append(min(b, c))
    else:
        DP.append(c)

    a = None
    b = None
    c = None

print(DP[n])
