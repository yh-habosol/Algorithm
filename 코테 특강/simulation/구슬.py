n, m, t = map(int, input().split())

arr = [[0] * n for _ in range(n)]
arr_new = [[0] * n for _ in range(n)] 

for i in range(m):
    r, c, d, w = map(str, input().split())
    r, c, w = int(r), int(c), int(w)
    arr[r-1][c-1] = [w, d, i]
    
    
def isSafe(i, j):
    global n
    if (i>=0 and i<n) and (j>=0 and j<n):
        return True
    return False

#구슬 하나 움직이는 함수
def move(i, j):
    if arr[i][j][1] == 'L':
        if isSafe(i, j-1):
            if arr_new[i][j-1] == 0:
                arr_new[i][j-1] = [arr[i][j][0], arr[i][j][1], arr[i][j][2]]
            else:
                if arr_new[i][j-1][2] > arr[i][j][2]:
                    arr_new[i][j-1] = [arr[i][j][0] + arr_new[i][j-1][0], arr_new[i][j-1][1], arr_new[i][j-1][2]]
                else:
                    arr_new[i][j-1] = [arr[i][j][0] + arr_new[i][j-1][0], arr[i][j][1], arr[i][j][2]]
        else:
            arr_new[i][j] = [arr[i][j][0], 'R', arr[i][j][2]]
    
    if arr[i][j][1] == 'R':
        if isSafe(i, j+1):
            if arr_new[i][j+1] == 0:
                arr_new[i][j+1] = [arr[i][j][0], arr[i][j][1], arr[i][j][2]]
            else:
                if arr_new[i][j+1][2] > arr[i][j][2]:
                    arr_new[i][j+1] = [arr[i][j][0] + arr_new[i][j+1][0], arr_new[i][j+1][1], arr_new[i][j+1][2]]
                else:
                    arr_new[i][j+1] = [arr[i][j][0] + arr_new[i][j+1][0], arr[i][j][1], arr[i][j][2]]
        else:
            arr_new[i][j] = [arr[i][j][0], 'L', arr[i][j][2]]
            
    if arr[i][j][1] == 'U':
        if isSafe(i-1, j):
            if arr_new[i-1][j] == 0:
                arr_new[i-1][j] = [arr[i][j][0], arr[i][j][1], arr[i][j][2]]
            else:
                if arr_new[i-1][j][2] > arr[i][j][2]:
                    arr_new[i-1][j] = [arr[i][j][0] + arr_new[i-1][j][0], arr_new[i-1][j][1], arr_new[i-1][j][2]]
                else:
                    arr_new[i-1][j] = [arr[i][j][0] + arr_new[i-1][j][0], arr[i][j][1], arr[i][j][2]]
        else:
            arr_new[i][j] = [arr[i][j][0], 'D', arr[i][j][2]]
            
    if arr[i][j][1] == 'D':
        if isSafe(i+1, j):
            if arr_new[i+1][j] == 0:
                arr_new[i+1][j] = [arr[i][j][0], arr[i][j][1], arr[i][j][2]]
            else:
                if arr_new[i+1][j][2] > arr[i][j][2]:
                    arr_new[i+1][j] = [arr[i][j][0] + arr_new[i+1][j][0], arr_new[i+1][j][1], arr_new[i+1][j][2]]
                else:
                    arr_new[i+1][j] = [arr[i][j][0] + arr_new[i+1][j][0], arr[i][j][1], arr[i][j][2]]

        else:
            arr_new[i][j] = [arr[i][j][0], 'U', arr[i][j][2]]
    
#구슬 전부 움직이는 함수
def moveAll():
    global n
    for i in range(n):
        for j in range(n):
            arr_new[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                move(i, j)
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr_new[i][j]
    print("one move: ")
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='       ')
        print("")
    print("")
    
    
def simulate():
    moveAll()



while t > 0:
    simulate()
    t -= 1

c = 0
m = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            c += 1
            if m < arr[i][j][0]:
                m = arr[i][j][0]
print(c, m)