n = int(input())

arr = [[0] * n for _ in range(n)]

c_left = 0
c_right = n-1
r_up = 0
r_down = n-1
cnt = n*n

x, y = n-1, n-1

while cnt >= 1:
    for i in range(c_right, c_left-1, -1):
        arr[x][i] = cnt
        cnt -= 1
        y -= 1
    r_down -= 1
    y = i
    for i in range(r_down, r_up-1, -1):
        arr[i][y] = cnt
        cnt -= 1
        x -= 1
    x = i
    c_left += 1
    for i in range(c_left, c_right+1):
        arr[x][i] = cnt
        cnt -= 1
        y += 1
    y = i
    r_up += 1
    for i in range(r_up, r_down+1):
        arr[i][y] = cnt
        cnt -= 1
        x += 1
    x = i
    c_right -= 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print("")
    
    