from collections import deque

n, k, u, d = map(int, input().split())

grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def InRange(x, y):
    global n
    return (x>=0 and x<n) and (y>=0 and y<n)

def canGo(cur_x, cur_y, new_x, new_y):
    global u, d
    return InRange(new_x, new_y) and visited[new_x][new_y]==0 and (u<=abs(grid[cur_x][cur_y]-grid[new_x][new_y])<=d)

def BFS():
    while len(q) != 0:
        v_x, v_y = q.popleft()
        for i in range(4):
            new_x = v_x + dx[i]
            new_y = v_y + dy[i]
            if canGo(v_x, v_y, new_x, new_y):
                visited[new_x][new_y] = 1
                
def num_city():
    global n
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                count += 1
    return count
                


q = deque()
M = []
index = []
for i in range(n):
    for j in range(n):
        index.append((i, j))

if k == 1:
    for i in range(n):
        for j in range(n):
            visited = [[0]*n for _ in range(n)]
            q.append((i, j))
            visited[i][j] = 1
            BFS()
            M.append(num_city())
elif k == 2:
    for i in range(len(index)-1):
        for j in range(i+1, len(index)):
            visited = [[0]*n for _ in range(n)]
            q.append(index[i])
            q.append(index[j])
            visited[index[i][0]][index[i][1]] = 1
            visited[index[j][0]][index[j][1]] = 1
            BFS()
            M.append(num_city())

elif k == 3:
    for i in range(len(index)-2):
        for j in range(i+1, len(index)-1):
            for k in range(j+1, len(index)):
                visited = [[0]*n for _ in range(n)]
                q.append(index[i])
                q.append(index[j])
                q.append(index[k])
                visited[index[i][0]][index[i][1]] = 1
                visited[index[j][0]][index[j][1]] = 1
                visited[index[k][0]][index[k][1]] = 1
                BFS()
                M.append(num_city())

print(max(M))