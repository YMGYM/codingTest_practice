n, m  = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

end = n
start = 0
mid = (start + end) // 2 

while (start <= end):
    dduck = 0
    mid = (start + end) // 2 

    for i in range(len(arr)):
        dduck += (arr[i] - arr[mid])
    print(dduck)
    if dduck == m:
        break
    elif dduck > m: # 떡이 너무 많이 잘렸을 때
        start = mid + 1
        print("change start", start, end)
    else:
        end = mid - 1
        print("change end", start, end)

print(arr[mid])