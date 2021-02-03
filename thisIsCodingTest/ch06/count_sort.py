# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 0 ~ 최대값 까지의 리스트 선언
count = [0] * (max(array)  + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)): # 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')
