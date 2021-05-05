expression = input()


max_cal = 0
alphabet_num = []
# for i in range(len(expression)):
#     if i %2 == 0:
#         alphabet_num.append(expression[i])
# alphabet_num = list(set(alphabet_num))


for i in range(len(expression)):
    if i % 2 == 0:
        if expression[i] not in alphabet_num:
            alphabet_num.append(expression[i])

answer = []
K = 4
N = len(alphabet_num)

def cal(li):
    dict_num = {alphabet_num[i]:li[i] for i in range(N)}
    num_arr = []
    operator_arr = []
    for i in range(len(expression)):
        if expression[i] in alphabet_num:
            if len(num_arr) == 0:
                num_arr.append(dict_num[expression[i]])
            else:
                a = num_arr.pop()
                b = dict_num[expression[i]]
                o = operator_arr.pop()
                if o == '+':
                    num_arr.append(a+ b)
                elif o == '-':
                    num_arr.append(a-b)
                elif o == '*':
                    num_arr.append(a*b)
        else:
            operator_arr.append(expression[i])
    return num_arr.pop()
                


def findPermutation(cnt):
    global max_cal
    if cnt == N:
        m = cal(answer)
        if m > max_cal:
            max_cal = m
        return
    
    for i in range(1, K+1):
        answer.append(i)
        findPermutation(cnt+1)
        answer.pop()

findPermutation(0)
print(max_cal)