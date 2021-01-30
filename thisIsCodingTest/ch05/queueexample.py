from collections import deque # queue 보다 빠른 자료구조

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft() # 5 가 삭제됨
queue.append(1)
queue.append(4)

queue.popleft()

print(queue)
queue.reverse() # 역순으로 출력
print(queue)