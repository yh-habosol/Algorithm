INF = float('inf')
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

#a노드에서 b노드로 c만큼의 비용이 듬.
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

#방문하지 않은 노드 중 최단거리가 가장 짧은 노드 인덱스 반환	
def get_smallest_node():
	min_value = INF
	index = 0
	for i in range(1, n+1):
		if visited[i] == False and min_value > distance[i]:
			index = i
			min_value = distance[i]
	return index


def dijkstra(start):
	distance[start] = 0
	visited[start] = True
	for j in graph[start]:
		distance[j[0]] = j[1]
	
	for i in range(n-1):
		now = get_smallest_node()
		visited[now] = True
		for j in graph[now]:
			cost = distance[now] + j[1]
			if cost < distance[j[0]]:
				distance[j[0]] = cost


dijkstra(start)
for i in range(1, n+1):
	if distance[i] == INF:
		print("Infinity")
	else:
		print(distance[i], end = ' ')
	
	
	