n = int(input())
have_num = list(map(int, input().split()))

m = int(input())
find_num = list(map(int, input().split()))

def bi_search(n, arr, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2
    if arr[mid] == n:
        return "yes"
    elif arr[mid] < n:
        return bi_search(n, arr, mid + 1, end)
    else:
        return bi_search(n, arr, start, mid - 1)


have_num.sort()
result = []
for i in range(m):

    result.append(bi_search(find_num[i], have_num, 0, n-1))

for j in range(m):
    print(result[j], end=' ')