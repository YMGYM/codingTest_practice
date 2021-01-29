# n = map(int, input().split())
# plan = list(input().split())

# pos = [1,1]
# for p in plan:
#     if p == 'U':
#         if pos[0] == 1:
#             continue
#         else:
#             pos[0] -= 1
#     elif p == 'D':
#         if pos[0] == n:
#             continue
#         else:
#             pos[0] += 1
#     elif p == 'L':
#         if pos[1] == 1:
#             continue
#         else:
#             pos[1] -= 1
#     elif p == 'R':
#         if pos[1] == n:
#             continue
#         else:
#             pos[1] += 1

# print(f"{pos[0]} {pos[1]}")

# 모범답안
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1] # 이동방향
dy = [-1, 1, 0 , 0]
move_types = ['L','R','U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
    x, y = nx, ny

print(x, y)