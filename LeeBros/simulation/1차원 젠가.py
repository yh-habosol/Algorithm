n = int(input())
block = []
for i in range(n):
    b = int(input())
    block.append(b)

s1, e1 = map(int,input().split())
s2, e2 = map(int,input().split())


temp = []
for i in range(n):
    if i<s1-1 or i>e1-1:
        temp.append(block[i])
block = temp
temp = []
for i in range(len(block)):
    if i < s2-1 or i > e2-1:
        temp.append(block[i])
block = temp

if len(block)==0:
    print(0)
else:
    print(len(block))
    for i in block:
        print(i)