n, m = map(int, input().split())

money = []

for i in range(n):
    money.append(int(input()))

money.sort() # 돈을 크기순으로 정렬

result = [10001] * 10001 # 가장 큰 금액으로 설정

result[0] = m # 기본 액수 설정

for i in range(1, m + 1): # 모든 돈이 1원이면 m+1번 반복할 것임
    for j in range(n):
        if result[i-1] - money[j] >= 0:
            result[i] = min(result[i], result[i-1] - money[j]) # 더 많이 빼는 수로 설정

    # print(result[i])    

    if result[i] == 0:
        print(i)
        break
    elif result[i] == 10001:
        print(-1)
        break