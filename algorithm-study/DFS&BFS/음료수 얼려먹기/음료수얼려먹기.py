N, M = map(int, input().split())
ice = []

for i in range(N):
  temp = list(map(int, input().split()))
  ice.append(temp)
  

def canGo(x, y):
	if x >= 0 and x<N and y>=0 and y<M and ice[x][y] == 0:
		return True
	else:
		return False
	
def dfs(x, y):
	if ice[x][y] == 1:
		return False
	
	ice[x][y] = 1
	graph = []
	
	if canGo(x-1, y):
		graph.append((x-1, y))
	if canGo(x, y-1):
		graph.append((x, y-1))
	if canGo(x, y+1):
		graph.append((x, y+1))
	if canGo(x+1, y):
		graph.append((x+1, y))
	
	for v in graph:
		dfs(v[0], v[1])
	return True

count = 0
for i in range(N):
	for j in range(M):
		if dfs(i, j):
			count += 1
print(count)