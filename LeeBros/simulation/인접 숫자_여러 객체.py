n, m, t = map(int, input().split())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

count = [[0]*n for _ in range(n)]
for i in range(m):
    r, c = map(int, input().split())
    count[r-1][c-1] = 1

next_count = [[0]*n for _ in range(n)]    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def isSafe(i, j):
    global n
    if (i>=0 and i<n) and (j>=0 and j<n):
        return True
    return False


def Move(x, y):
    max_num, max_pos = 0, (0,0)
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if isSafe(next_x, next_y) and arr[next_x][next_y]>max_num:
            max_num = arr[next_x][next_y]
            max_pos = (next_x, next_y)
    x, y = max_pos
    next_count[x][y] += 1
    
    
def moveAll():
    global n
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                Move(i, j)
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]
    
def removeDuplicateMarbles():
    global n
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

def Simulate():
    moveAll()
    removeDuplicateMarbles()
    
while t>0:
    Simulate()
    t -= 1
            
c = 0

for i in range(n):
    for j in range(n):
        if count[i][j]==1:
            c += 1
print(c)
            