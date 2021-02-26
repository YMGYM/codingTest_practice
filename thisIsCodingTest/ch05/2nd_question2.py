from collections import deque

n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

# cnt = [[0] * m for _ in range(n)]

que = deque()

que.append((0,0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    x, y = que.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue

        if maps[new_x][new_y] == 0:
            continue

        if maps[new_x][new_y] == 1:
            maps[new_x][new_y] = maps[x][y] + 1
            que.append((new_x, new_y))


print(maps)
print(maps[n-1][m-1])

    


