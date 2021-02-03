n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input())) # 배열에 input 원소 추가

arr.sort() # 배열 정렬
arr.reverse() # 배열 반전

for a in arr:
    print(a, end=' ') # 원소를 하나씩 출력