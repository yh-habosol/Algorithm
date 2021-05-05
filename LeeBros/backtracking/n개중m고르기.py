n, m = map(int, input().split())

dots = []
for i in range(n):
    x, y = map(int, input().split())
    dots.append((x, y, i))

answer = []
    
M = float('inf')
def cal(li):
    global M
    temp = 0
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if pow(abs(li[i][0]-li[j][0]),2) + pow(abs(li[i][1]-li[j][1]),2) > temp:
                temp = pow(abs(li[i][0]-li[j][0]),2) + pow(abs(li[i][1]-li[j][1]),2)
    if M > temp:
        M = temp
def find_min(cnt):
    if cnt == m:
        cal(answer)
        return

    for i in range(n):
        if dots[i] in answer:
            continue
        if answer:
            if answer[-1][2] > dots[i][2]:
                continue
        answer.append(dots[i])
        find_min(cnt + 1)
        answer.pop()

find_min(0)
print(M)