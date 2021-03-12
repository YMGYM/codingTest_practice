n = int(input())
card_p = list(map(int, input().split()))

dp = [0] * (n + 1) # 카드를 살 가격의 최대값을 만드는 dp 테이블 작성

for i in range(1, len(card_p) + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
    dp[i] = max(dp[i], card_p[i-1])


for p in range(len(card_p) + 1 , n):
    for i in range(1, p):
        dp[p] = max(dp[p], dp[i] + dp[p - i])

print(dp[n])