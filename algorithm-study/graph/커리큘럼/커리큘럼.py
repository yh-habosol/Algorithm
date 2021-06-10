from collections import deque
import copy

N = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
time = [0] * (N+1)

for i in range(1, N+1):
    inp = list(map(int, input().split()))
    time[i] = inp[0]
    for j in inp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1




def topological_sort():
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()

        for i in graph[node]:
            indegree[i] -= 1
            result[i] = max(result[i], result[node] + time[i])
            if indegree[i] == 0:
                q.append(i)
                
    print(result)

topological_sort()


