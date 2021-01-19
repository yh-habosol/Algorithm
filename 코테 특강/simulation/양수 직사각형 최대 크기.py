n, m = map(int, input().split())

arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)


def find(idx, idy, size_x,size_y):
    global n
    global m
    if idx + size_x > n or idy + size_y >m:
        return False
    for i in range(idx, idx + size_x):
        for j in range(idy, idy + size_y):
            if arr[i][j] <= 0:
                return False
    return True
    
def is_positive(r, c):
    global n
    global m
    for i in range(n):
        for j in range(m):
            if find(i, j, r, c):
                return r*c
    return False

ans = -1

for i in range(1, n+1):
    for j in range(1, m+1):
        if is_positive(i, j):
            if is_positive(i, j) > ans:
                ans = is_positive(i, j)

print(ans)