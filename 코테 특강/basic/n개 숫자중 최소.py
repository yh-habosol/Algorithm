n = int(input())
L = list(map(int, input().split()))

count = 0
m = L[0]
for i in range(1, len(L)):
    if L[i] < m:
        m = L[i]
for i in L:
    if i == m:
        count += 1
print(m, count)