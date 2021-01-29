# input = input()
# x, y = input[0], input[1]

# xs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# ys = ['1', '2', '3', '4', '5', '6', '7', '8']

# cnt = 0
# xi = xs.index(x)
# yi = ys.index(y)

# # 왼쪽으로 두 칸 이동
# if xi - 2 >= 0:
#     if yi - 1 >= 0:
#         cnt += 1
#     if yi + 1 < 8:
#         cnt += 1

# # 오른으로 두 칸 이동
# if xi + 2 < 8:
#     if yi - 1 >= 0:
#         cnt += 1
#     if yi + 1 < 8:
#         cnt += 1

# # 위쪽으로 두 칸 이동
# if yi - 2 >= 0:
#     if xi - 1 >= 0:
#         cnt += 1
#     if xi + 1 < 8:
#         cnt += 1

# # 아래쪽으로 두 칸 이동
# if yi + 2 < 8:
#     if xi - 1 >= 0:
#         cnt += 1
#     if xi + 1 < 8:
#         cnt += 1

# print(cnt)

# 모범답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, -2), (1,2), (-1, -2), (-1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 가능하다면
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)