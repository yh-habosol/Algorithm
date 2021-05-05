N = int(input())

stair = []

for i in range(N):
    n = int(input())
    stair.append(n)


def findMax():
    global N

    if N == 1:
        return stair[0]
    elif N == 2:
        return stair[0]+stair[1]

    DP = [stair[0], stair[0]+stair[1],
          max(stair[0] + stair[2], stair[1]+stair[2])]
    count = 2

    for i in range(3, N):
        if count == 2:
            if DP[i-2]+stair[i] > DP[i-3] + stair[i-1] + stair[i]:
                DP.append(DP[i-2]+stair[i])
                count = 1
            else:
                DP.append(DP[i-3] + stair[i-1] + stair[i])
                count = 2
        elif count < 2:
            if max(DP[i-1] + stair[i], DP[i-2]+stair[i], DP[i-3] + stair[i-1] + stair[i]) == DP[i-1] + stair[i]:
                DP.append(DP[i-1] + stair[i])
                count += 1
            elif max(DP[i-1] + stair[i], DP[i-2]+stair[i], DP[i-3] + stair[i-1] + stair[i]) == DP[i-2]+stair[i]:
                DP.append(DP[i-2] + stair[i])
                count = 1
            elif max(DP[i-1] + stair[i], DP[i-2]+stair[i], DP[i-3] + stair[i-1] + stair[i]) == DP[i-3] + stair[i-1] + stair[i]:
                DP.append(DP[i-3] + stair[i-1] + stair[i])
                count = 2
    return DP[-1]


print(findMax())
