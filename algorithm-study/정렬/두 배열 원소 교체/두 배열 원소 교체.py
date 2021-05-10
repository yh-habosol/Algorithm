N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

index = 0
for i in range(K):
    if A[index] < B[i]:
        A[index], B[i] = B[i], A[index]
        index += 1
print(sum(A))