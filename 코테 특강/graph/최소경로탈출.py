from collections import deque

n, m = map(int, input().split())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]


M = float('inf')
q = deque()

def InRange(x, y):
    global n, m
    return (x>=0 and x<n) and (y>=0 and y<m)

def CanGo(x, y):
    return InRange(x, y) and visited[x][y] == 0 and grid[x][y]==1

def Push(x, y, new_step):
    q.append((x, y))
    visited[x][y] = 1
    step[x][y] = new_step
    
def findMin():
    global n,m, M
    while len(q) != 0:
        v_x, v_y = q.popleft()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]
            if CanGo(new_x, new_y):
                Push(new_x, new_y, step[v_x][v_y] + 1)
    if visited[n-1][m-1]:
        M = step[n-1][m-1]
    
Push(0,0,0)
findMin()
if M == float('inf'):
    print(-1)
else:
    print(M)

            