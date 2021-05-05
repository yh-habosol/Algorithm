N, M = map(int, input().split())

card = []

for i in range(N):
  temp = list(map(int, input().split()))
  card.append(temp)

min_list = []

for li in card:
  min_list.append(min(li))

print(max(min_list))