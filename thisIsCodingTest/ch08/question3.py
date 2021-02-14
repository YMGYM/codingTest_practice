n = int(input())

badak = [0] * n # 넓이만큼 배열 생성

"""
1 * 2 바닥 : 1
2 * 1 바닥 : 2
2 * 2 비닥 : 3
"""

## jvuf3jdz
answer = (n // 3) * 5

if n // 3 == 0:
    print(answer)
elif n // 3 == 1:
    print(answer + 1)
else n // 3 == 2:
    print(answer + 2)
