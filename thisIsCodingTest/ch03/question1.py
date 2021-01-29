# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# arr.reverse()

# cnt = 0
# result = 0

# for i in range(M):
#     if cnt < K:
#         result += arr[0]
#         cnt += 1
#     else:
#         result += arr[1]
#         cnt = 0

# print(result)

# 더 개선된 방법
n, m ,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[n-1]
second = arr[n-2]

count = int(m / (k + 1) ) * k
count += m % (k + 1) # 나누어 떨어지지 않는 경우도 고려한다.

result = 0
result += count * first
result += (m - count) * second

print(result)



