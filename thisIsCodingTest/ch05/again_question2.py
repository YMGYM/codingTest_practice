from collections import deque

n, m = map(int, input().split())

mapping = []

for i in range(n):
    # 맵 인풋
    mapping.append(list(map(int, input())))


queue = deque()

print(mapping)

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def bfs():
    queue.append((0, 0))

    while queue: # queue 가 남아 있을때까지 반복
        
        print(queue)
        x, y = queue.popleft()


        for i in range(4):
                
            nx = x + dxs[i]
            ny = y + dys[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if mapping[nx][ny] == 1:
                mapping[nx][ny] = mapping[x][y] + 1
                queue.append((nx, ny))


bfs()
print(mapping[n-1][m-1])