N , M = map(int, input().split())

answer = []

def choose(cnt):
    if cnt == M:
        print(*answer)
        return
    for i in range(1, N+1):
        if i in answer:
            continue
        # if answer:
        #     if answer[-1] > i:
        #         continue 
        answer.append(i)
        choose(cnt+1)
        answer.pop()


choose(0)
