def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스 + 1로 반환한다)

print("input: ")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("Input String:")
array = input().split()

print(sequential_search(n, target, array))

