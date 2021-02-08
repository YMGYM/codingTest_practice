# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)

# print(fibo(4))

# 다이나믹 프로그래밍 적인 방법
# 메모이제이션을 위한 리스트 초기화
d = [0] * 100

# 탑다운 다이나믹 프로그래밍
def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x] # 이미 계산한 적이 있으면 그래도 반환

    # 아직 계산하지 않은 문제라면 점화식에 따라 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))