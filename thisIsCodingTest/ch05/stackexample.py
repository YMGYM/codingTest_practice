# 후입 선출 방식의 자료구조
# 라이브러리 사용 없이 메소드로 사용 가능.

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop() # 7이 빠진다.

stack.append(1)
stack.append(4)
stack.pop() # 4가 빠진다.

print(stack)
print(stack[::-1])