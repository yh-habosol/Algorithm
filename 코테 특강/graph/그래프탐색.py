N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False]*N
def DFS(v):
    visited[v] = True
    for w in graph[v]:
        if visited[w] == False:
            DFS(w)

DFS(0)
count = 0
for i in visited:
    if i == True:
        count += 1
print(count-1)