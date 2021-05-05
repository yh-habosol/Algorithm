def distance(a, b):
    return abs(a) + abs(b)


N = int(input())
dists = []

for i in range(N):
    a, b = map(int, input().split())
    dist = distance(a, b)
    dists.append((dist, i+1))
dists.sort(key = lambda x: (x[0], x[1]))
for dist in dists:
    print(dist[1])