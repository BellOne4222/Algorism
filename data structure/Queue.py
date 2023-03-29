from collections import deque # 큐의 상위 버전(양방향, 맨 뒤 맨 앞 다 값을 넣거나 뺄 수 있음)

#appendleft() -> 왼쪽으로 값을 넣는 것
dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)
print(dq)

print(dq.pop())
print(dq.popleft())

#deque([789, 456, 123]) 123 789