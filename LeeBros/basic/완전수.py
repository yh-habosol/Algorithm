start, end = map(int, input().split())

def find_num(n):
    count = 0
    for i in range(1, n):
        if n%i==0:
            count += i
    return count


count = 0
for i in range(start, end+1):
    n = find_num(i)
    if n == i:
        count += 1
print(count)