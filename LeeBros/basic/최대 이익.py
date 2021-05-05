n = int(input())
L = list(map(int, input().split()))

m = 0
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        if L[j]-L[i] > m:
            m = L[j] - L[i]
print(m)