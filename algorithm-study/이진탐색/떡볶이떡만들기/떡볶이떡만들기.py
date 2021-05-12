N, M = map(int, input().split())
ricecake = list(map(int, input().split()))

big = max(ricecake)

height = []

def findM(array, length):
	s = 0
	for i in array:
		if length < i:
			s += (i-length)
	return s

def findmax(ricecake, start, end):
	while start<=end:
		mid = (start+end) // 2
		if findM(ricecake, mid) >= M:
			height.append(mid)
			start = mid + 1
		else:
			end = mid - 1
findmax(ricecake, 0,  big)
print(height[-1])