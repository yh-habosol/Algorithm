N, M = map(int, input().split())
ricecake = list(map(int, input().split()))

big = max(ricecake)
temp = [i for i in range(big+1)]

height = []

def findM(array, length):
    sum = 0
    for i in array:
        if length < i:
            sum += (i-length)
    return sum
