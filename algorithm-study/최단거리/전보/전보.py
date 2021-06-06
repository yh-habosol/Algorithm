import heapq

INF = float('inf')
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance= [INF] * (N+1)


for i in range(1, M+1):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

count = 0
max_value = 0

for d in distance:
    if d != INF:
        count += 1
        max_value = max(d, max_value)
print(count-1, max_value)