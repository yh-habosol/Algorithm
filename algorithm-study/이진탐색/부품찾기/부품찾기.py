N = int(input())
part = list(map(int, input().split()))
M = int(input())
need = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1 
        else:
            start = mid + 1
    return None

part.sort()

for i in need:
    if binary_search(part, i, 0, len(part)-1):
        print("YES", end = ' ')
    else:
        print("NO", end = ' ')