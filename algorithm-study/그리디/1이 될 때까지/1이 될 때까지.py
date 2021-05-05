N, K = map(int, input().split())

count = 0

# while True:
#   if N == 1:
#     break
#   if N % K == 0:
#     N = N // K
#   else:
#     N -= 1
#   count += 1

# print(count)


while True:
  target = (N//K)*K
  count += N - target
  N = target

  if N < K:
    break
  count += 1
  N = N//K

count += (N-1)

print(count)