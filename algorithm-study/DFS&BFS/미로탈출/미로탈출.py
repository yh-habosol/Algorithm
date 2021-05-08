from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
	temp = list(map(int, input().split()))
	graph.append(temp)
	

# def canGo(x, y):
# 	if x>=0 and x<N and y>=0 and y<M and graph[x][y] == 1 and visited[x][y] == 0:
# 		return True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# visited = [[0 for _ in range(M)] for _ in range(N)]

	
# def bfs(x, y):
# 	count = 0
# 	queue = deque()
# 	queue.append((0,0))
# 	visited[0][0] = 1
# 	toss = 0
	
# 	while True:
# 		toss = 0
# 		nx, ny = queue.popleft()
# 		if nx == N-1 and ny == M-1:
# 			count += 1
# 			break
# 		for i in range(4):
# 			nxx = nx + dx[i]
# 			nyy = ny + dy[i]
# 			if canGo(nxx, nyy):
# 				queue.append((nxx, nyy))
# 				visited[nxx][nyy] = 1
# 				toss += 1
# 		count += 1
# 		if toss == 0:
# 			count -= 1
# 		print("count: ", count)
# 		print("nx, ny: ", nx, ny)
# 		print()
# 	return count

# n = bfs(0,0)
# print(n)

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	
	while queue:
		x, y = queue.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx<0 or nx>=N or ny<0 or ny>=M:
				continue
			if graph[nx][ny] == 0:
				continue
			if graph[nx][ny] == 1:
				queue.append((nx, ny))
				graph[nx][ny] = graph[x][y] + 1
	return graph[N-1][M-1]
	
	
print(bfs(0,0))
