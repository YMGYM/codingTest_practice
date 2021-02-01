n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))


def dfs(x, y):
    cnt = 0


    if x < 0 or x >= n or y < 0 or y >= m:

        return False
    
    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False
    

cnt = 0
for x in range(n):
    for y in range(m):
        chk = dfs(x, y)
        if chk == True:
            cnt += 1

print(cnt)
