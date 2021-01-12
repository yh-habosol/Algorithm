import sys
N = int(sys.stdin.readline())
result = []

for k in range(N):
    n = int(sys.stdin.readline())
    tel = []
    for _ in range(n):
        tel.append(sys.stdin.readline().rstrip("\n"))
    tel.sort()
    for i in range(len(tel)):
        if i != len(tel)-1:
            if tel[i] == tel[i+1][0:len(tel[i])]:
                result.append("NO")
                break
        if i == len(tel)-1:
            result.append("YES")


for i in result:
    print(i)
