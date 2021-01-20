n = int(input())
li = list(map(int, input().split()))

m = float('inf')
count = 0

def jump(cnt):
    global m, count
    if cnt == n-1:
        if m > count:
            m = count
        return
    elif cnt >= n:
        return
    if li[cnt]==0 and cnt < n-1:
        return
    
    for i in range(1, li[cnt]+1):       
        count += 1
        jump(cnt + i)
        count -= 1
        

        
jump(0)         
if m == float('inf'):
    print(-1)
else:
    print(m)