N, K = map(int, input().split())
price = []
for i in range(N):
    n = int(input())
    price.append(n)
count = 0

temp = 0
M = len(price)-1

while K != 0:
    for i in range(M, -1, -1):
        if price[i] <= K:
            temp = i
            break
    n = K//price[temp]
    count += n
    K = K % price[temp]
    M = temp
print(count)
