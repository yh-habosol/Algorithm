N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

sum = 0
count = 0

num_list.sort()

large = num_list[-1]
second = num_list[-2]

#####################################
#O(n)
# for _ in range(M):
#   if count == K:
#     sum += second
#     count = 0
#   else:
#     sum += large
#     count += 1

# print(sum)
#####################################


######################################
#O(1)
count = (M//(K+1))*K
count += M%(K+1)

 
sum += large*count
sum += second*(M-count)
######################################
print(sum)