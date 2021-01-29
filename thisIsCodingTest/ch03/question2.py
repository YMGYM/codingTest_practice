# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(min(list(map(int, input().split()))))

# print(max(arr))

# 모범답안
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)

#     result = max(result, min_value)

# print(result)

# 이중반복문을 사용한 답안
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 1001 # 임의의 큰 값 대입
    for j in data:
        min_value = min(min_value, j)
    result = max(result, min_value)

print(result)