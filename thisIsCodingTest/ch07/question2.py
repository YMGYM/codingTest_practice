# n, m = map(int, input().split())
# dduck = list(map(int, input().split()))

# dduck.sort()
# height = dduck[n-1]

# flag = True

# while flag:
#     result = 0
#     for i in dduck:
#         result += max(0, i - height)

#     if result >= m:
#         flag = False
#         print(height)
#     else:
#         height -= 1

# 모범답안 예시
n, m  = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
    if total < m: # 떡이 덜 잘렸을 경우(왼쪽으로 이동)
        end = mid - 1
    else: # 떡이 더 잘렸을 경우 (오른쪽으로 이동)
        result = mid # 최대한 덜 잘랐을 때가 정답이므로..
        start = mid + 1

print(result)