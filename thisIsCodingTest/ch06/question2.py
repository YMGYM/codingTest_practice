n = int(input())

students = []

for i in range(n):
    input_data = input().split()
    name, score = input_data[0], int(input_data[1])

    students.append({'name':name, 'score':score})


result = sorted(students, key=(lambda x: x['score']))

for i in range(n):
    print(result[i]['name'], end=' ')