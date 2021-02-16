n = int(input())

k = list(map(int, input().split()))

ans = [0] * 100

ans[0] = k[0]
ans[1] = max(k[0], k[1])

for i in range(2, n):
    ans[i] = max(ans[i-1], ans[i-2] + k[i]) # 앞 경우에

print(ans[n-1])