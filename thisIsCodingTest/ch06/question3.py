n, k = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# 나의 알고리즘
# for _ in range(k):
#     max_item = max(arrB)
#     arrA.append(max_item)
#     arrB.remove(max_item)

#     min_item = min(arrA)
#     arrA.remove(min_item)
#     arrB.append(min_item)

# 모범 답안
arrA.sort()
arrB.sort(reverse=True)

for i in range(K):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

    else:
        break


print(sum(arrA))




