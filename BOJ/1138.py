N = int(input())

height = list(map(int, input().split()))
align = [None]*N
index = list(range(N))

for i in range(len(height)):
    n = height[i]
    k = index.pop(n)
    align[k] = i+1

print(*align)
