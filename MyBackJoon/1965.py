n = int(input())

boxes = list(map(int, input().split()))

dp = [1] * n # 모든 상자는 자기 자신을 포함해 1

for i in range(n):
    for j in range(0, i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))