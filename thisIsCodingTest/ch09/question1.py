n, m = map(int, input().split())
INF = 1e9

# 배열 초기화
city = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 경로는 0으로 초기화
for i in range(n + 1):
    city[i][i] = 0

# 이방법보다 위에가 낫지 않나?
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             city[a][b] = 0

# 간선에 대한 정보를 입력받아 초기화
for _ in range(m):
    a, b = map(int, input().split())
    city[a][b] = 1
    city[b][a] = 1

# 목표회사 정보
x, k = map(int, input().split())

# 플로이드 - 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            city[a][b] = min(city[a][b], city[a][k] + city[k][b])


if city[1][k] >= INF or city[k][x] >= INF:
    print(-1)
else:
    print(city[1][k] + city[k][x])