n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

def is_safe(i, j):
    global n
    if (i>=0 and i<n) and (j>=0 and j<n):
        return True
    return False

t = 0
def next_index(i, j, distance):
    global t
    if arr[i][j] == 0:
        if distance == 1:
            i += 1
        elif distance == 2:
            j -= 1
        elif distance == 3:
            i -= 1
        elif distance == 4:
            j += 1
    elif arr[i][j] == 1:
        if distance == 1:
            j -= 1
            distance = 2
        elif distance == 2:
            i += 1
            distance = 1
        elif distance == 3:
            j += 1
            distance = 4
        elif distance == 4:
            i -= 1
            distance = 3
    elif arr[i][j] == 2:
        if distance == 1:
            j += 1
            distance = 4
        elif distance == 2:
            i -= 1
            distance = 3
        elif distance == 3:
            j -= 1
            distance = 2
        elif distance == 4:
            i += 1
            distance = 1
    t += 1
    return i, j, distance

def cal_time(i, j, distance):
    global t
    while True:
        i, j, distance = next_index(i, j, distance)
        if is_safe(i, j) == False:
            t += 1
            return t

m = 0
for i in range(4):
    for k in range(n):
        temp = cal_time(0, k, 1)
        if m < temp:
            m = temp
        t = 0
    for k in range(n):
        temp = cal_time(k, n-1, 2)
        if m < temp:
            m = temp
        t = 0
    for k in range(n):
        temp  = cal_time(n-1, k, 3)
        if m < temp:
            m = temp
        t = 0
    for k in range(n):
        temp = cal_time(k, 0, 4)
        if m < temp:
            m = temp
        t = 0

print(m)