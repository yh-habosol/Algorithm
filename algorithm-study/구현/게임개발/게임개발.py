N, M = map(int, input().split())
x, y, d = map(int, input().split())

m = []
for i in range(N):
  temp = list(map(int, input().split()))
  m.append(temp)

m[x][y] = 2
  
dx = [-1,0,1,0]
dy = [0,-1,0,1]

count = 1

#true라면 방문, false라면 방문 안함.
def canGo(x, y):
  if m[x][y] == 0:
    return True
  else:
    return False

def check_4_ways(x, y):
  if canGo(x+1, y) == False and canGo(x-1, y) == False and canGo(x, y+1) == False and canGo(x, y-1) == False :
    return True
    
while True:
  d = (d+3)%4
  nx = x + dx[d]
  ny = y + dy[d]

  if canGo(nx, ny):
    print("x, y: ", x, y)
    x, y = nx, ny
    print("x, y: ", x, y)
    count += 1
    m[x][y] = 2

  if check_4_ways(x, y):
    temp_d = (d+2) % 4
    nx = x + dx[temp_d]
    ny = y + dy[temp_d]
    if m[nx][ny] == 1:
      break
    
print(count)
  
