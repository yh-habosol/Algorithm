n, m = map(int, input().split())

grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)
    
visited = [[0]*m for _ in range(n)]

dx = [1,0]
dy = [0,1]

def InRange(x, y):
    global n, m
    return (x>=0 and x<n) and (y>=0 and y<m)

def canGo(x, y):
    if InRange(x, y) == False:
        return False
    if visited[x][y] == 1 or grid[x][y]==0:
        return False
    return True

def find(x, y):
    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if canGo(new_x, new_y):
            visited[new_x][new_y] = 1
            find(new_x, new_y)

visited[0][0] = 1
find(0,0)
print(visited[n-1][m-1])