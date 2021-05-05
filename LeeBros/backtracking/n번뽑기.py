K, N = map(int, input().split())

answer = []

def findPermutation(cnt):
    if cnt == N:
        print(*answer)
        return
    
    for i in range(1, K+1):
        answer.append(i)
        findPermutation(cnt+1)
        answer.pop()

findPermutation(0)