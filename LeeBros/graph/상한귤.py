from collections import deque

n, k = map(int, input().split())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)

step = [[-1]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def InRange(x, y):
    global n
    return (x>=0 and x<n) and (y>=0 and y<n)

def CanGo(x, y):
    return InRange(x, y) and visited[x][y] == 0 and grid[x][y]==1

def Push(x, y, new_step):
    q.append((x, y))
    visited[x][y] = 1
    step[x][y] = new_step

def BFS():
    while len(q) != 0:
        v_x, v_y = q.popleft()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]
            if CanGo(new_x, new_y):
                Push(new_x, new_y, step[v_x][v_y]+1)

q = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            Push(i, j, 0)


BFS()
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and grid[i][j] == 1:
            step[i][j]= -2
        print(step[i][j], end = ' ')
    print()