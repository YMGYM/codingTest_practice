n = int(input())

badak = [0] * 1001 # 넓이만큼 배열 생성

"""
1 * 2 바닥 : 1
2 * 1 바닥 : 2
2 * 2 비닥 : 3
"""

# ## 오답이다
# answer = (n // 3) * 5

# if n // 3 == 0:
#     print(answer)
# elif n // 3 == 1:
#     print(answer + 1)
# else n // 3 == 2:
#     print(answer + 2)

# 정답

badak[1] = 1 # 1가지 뿐...
badak[2] = 3 # 경우의 수가 3가지

for i in range(3, n+1):
    badak[i] = (badak[i-1] + 2*badak[i-2]) % 796796


print(badak[n])