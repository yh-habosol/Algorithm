K, N = map(int, input().split())

answer = []

def findPermutation(cnt):
    if cnt == N:
        print(*answer)
        return
    
    for i in range(1, K+1):
        if cnt >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        else:
            answer.append(i)
            findPermutation(cnt+1)
            answer.pop()

findPermutation(0)