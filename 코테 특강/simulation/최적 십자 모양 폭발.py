import copy

n = int(input())

arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

def col_boom_one(row, col):
    global n
    temp = [None]
    for i in range(n): 
        if i == row:
            continue    
        temp.append(arr[i][col])
    return temp


def col_boom_many(row, col, count):
    global n
    if 2*count -1 >= n:
        return [None]*n

    temp = [None] * (2*count-1)
    for i in range(n):
        if i < row-(count-1) or i > row+(count-1):
            temp.append(arr[i][col])
    return temp


def col_copy(row, col, cols):
    global n
    for i in range(n):
        arr[i][col] = cols[i]

def boom(i, j):
    global n
    num = arr[i][j]
    for c in range(j-(num-1), j+(num-1) + 1):
        if c<0 or c>=n:
            continue
        if c == j:
            col = col_boom_many(i, c, num)
        else:
            col = col_boom_one(i, c)
        col_copy(i, c, col)
    
    

def find_adj():
    global n
    count = 0
    for i in range(n):
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1] and arr[i][j] != None:
                count += 1
    for i in range(n-1):
        for j in range(n):
            if arr[i][j] == arr[i+1][j] and arr[i][j] != None:
                count += 1
    return count


a = copy.deepcopy(arr)

m_count = 0
for i in range(n):
    for j in range(n):
        boom(i, j)
        if m_count < find_adj():
            m_count = find_adj()
        arr = copy.deepcopy(a)
print(m_count)