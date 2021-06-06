import heapq

INF = float('inf')
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

time_1_to_K = 0
time_K_to_X = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0 

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

time_1_to_K = graph[1][K]
time_K_to_X = graph[K][X]

if time_1_to_K == INF or time_K_to_X == INF:
    print(-1)
else:
    print(time_1_to_K + time_K_to_X)