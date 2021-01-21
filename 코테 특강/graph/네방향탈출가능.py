from collections import deque

n, m = map(int, input().split())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*m for _ in range(n)]

q = deque()
q.append((0,0))
visited[0][0] = 1

def Inrange(x, y):
    global n, m
    return (x>=0 and x<n) and (y>=0 and y<m)

def canGo(x, y):
    return Inrange(x, y) and visited[x][y]==0 and grid[x][y]==1

def BFS():
    while len(q) != 0:
        v_x, v_y = q.popleft()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]
            if canGo(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
BFS()
print(visited[n-1][m-1])