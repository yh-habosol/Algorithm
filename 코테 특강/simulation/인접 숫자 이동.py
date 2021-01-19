n, r, c = map(int, input().split())
r -= 1
c -= 1
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

def is_safe(i, j):
    global n
    if (i>=0 and i<n) and (j>=0 and j<n):
        return True
    return False

def canGo(i, j, cur_num):
    if is_safe(i, j) and arr[i][j] > cur_num:
        return True
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]


dist = []
count = 0
while True:
    count = 0
    for i in range(4):
        next_x = r + dx[i]
        next_y = c + dy[i]
        
        if canGo(next_x, next_y, arr[r][c]):
            dist.append(arr[r][c])
            r = next_x
            c = next_y
            break
        count += 1

    if count == 4:
        dist.append(arr[r][c])
        break
print(*dist)
    
    