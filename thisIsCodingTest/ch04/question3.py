n, m = map(int, input().split())
a, b, d = map(int, input().split())

mapping = []
cnt = 1
ways = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(n):
    mapping.append(list(map(int, input().split())))

for i in range(3):
    dx, dy = ways[d % 4]
    
    if mapping[a + dy][b + dx] == 0:
        a += dy
        b += dy
        cnt += 1
    else:
        d += 1

print(cnt)