# n, k = map(int, input().split())

# cnt = 0
# while True:
#     if n == 1:
#         break

#     if n >= k:
#         cnt += (n % k) + 1
#         n = (n // k)
#     else:
#         cnt += n -1
#         n = 1

# print(cnt)
    
# 모범 답안
# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     # 나누어 떨어지지 않는다면 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     # k로 나누기
#     n //= k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)

# 모범답안2
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break

    result += 1
    n //= k
    
result += (n-1)
print(result)