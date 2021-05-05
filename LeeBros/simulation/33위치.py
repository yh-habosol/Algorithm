N = int(input())
arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

def num_coin(i, j):
    count = 0
    for row in range(i, i+3):
        for col in range(j, j+3):
            if arr[row][col] == 1:
                count += 1
    return count

m = 0
for i in range(N):
    for j in range(N):
        if i + 2 >= N or j + 2 >= N:
            continue
        if num_coin(i, j) > m:
            m = num_coin(i, j)
print(m)