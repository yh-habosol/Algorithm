s, n = map(str, input().split())
n = int(n)
order = []
for i in range(n):
    num = int(input())
    order.append(num)

for i in order:
    if i==1:
        s = s[1:] + s[:1]
        print(s)
    elif i == 2:
        s = s[len(s)-1:] + s[:len(s)-1]
        print(s)
    elif i == 3:
        temp = ""
        for j in range(len(s)-1, -1, -1):
            temp += s[j]
        s = temp
        print(s)
        