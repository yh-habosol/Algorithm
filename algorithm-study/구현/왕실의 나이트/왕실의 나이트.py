position = input()

row = int(position[1])
col = ord(position[0]) - ord('a') +1 

dx = [2,2,-2,-2,1,-1,-1,1]
dy = [-1,1,-1,1,2,2,-2,-2]

count = 0

for i in range(len(dx)):
  if 1<= row + dx[i] <= 8 and 1 <= col + dy[i] <= 8:
    count += 1
print(count)