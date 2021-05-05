N = int(input())
students = []
for i in range(N):
    height, weight = map(int, input().split())
    students.append((height, weight, i+1))

students.sort(key = lambda x:(x[0], x[1], -x[2]), reverse = True)
for student in students:
    print(student[0], student[1], student[2])