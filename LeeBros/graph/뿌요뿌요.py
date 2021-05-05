n = int(input())

grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)

def InRange(x, y):
    global n
    return (x>=0 and x<n) and (y>=0 and y<n)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find(x, y, num):
    global count
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if InRange(new_x, new_y) and visited[new_x][new_y]==0:
            if grid[new_x][new_y] == num:
                count += 1
                visited[new_x][new_y] = 1
                find(new_x, new_y, num)

dic = {i:0 for i in range(1, 101)}
count = 0

for i in range(n):
    for j in range(n):
        visited = [[0]*n for _ in range(n)]
        num = grid[i][j]
        visited[i][j] = 1
        count += 1
        find(i, j, num)
        if dic[num] == 0:
            dic[num] = count
        else:
            dic[num] = max(count, dic[num])
        count = 0

m = 0
c = 0

for i in range(1, 101):
    if dic[i]>=4:
        c += 1
    if dic[i]>m:
        m = dic[i]

print(c, m)