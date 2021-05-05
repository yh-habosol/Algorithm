def len_RLE(s):
    RLE = ""
    index = 0
    num = 0
    end = False
    while True:
        if len(s) ==1:
            RLE = s[0] + str(1)
            break
        ch = s[index]
        count = 1
        for i in range(index+1, len(s)):
            if i == len(s)-1:
                end = True
            if s[i] == ch:
                count += 1
            else:
                index = i
                break
        RLE += (ch+str(count))

        if index>=len(s)-1 or end==True:
            if s[-2] != s[-1]:
                RLE += (s[-1]+str(1))
            break
    return len(RLE)


s = input()
m = float('inf')

if len(s) == 1:
    m = 2
else:
    for i in range(len(s)-1):
        s = s[1:] + s[0]
        if len_RLE(s) < m:
            m = len_RLE(s)
print(m)
