def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())

edges = []
parent = [0] * (N+1)
result = 0
m = 0

for i in range(N+1):
    parent[i] = i

for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        m = cost
        union_parent(parent, a, b)
        result += cost


print(result - m)