n, t = map(int, input().split())
arr = []
for i in range(2):
    te = list(map(int, input().split()))
    arr.append(te)
arr[1].reverse()

while t > 0:
    temp = arr[0][n-1]
    for i in range(n-1, 0, -1):
        arr[0][i] = arr[0][i-1]
    arr[0][0] = arr[1][0]
    
    for i in range(n-1):
        arr[1][i] = arr[1][i+1]
    arr[1][n-1] = temp
    
    t -= 1

arr[1].reverse()
for i in range(2):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print("")