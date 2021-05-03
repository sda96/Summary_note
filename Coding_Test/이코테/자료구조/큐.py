# 선입선출
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(8)
queue.popleft()
queue.popleft()
queue.append(9)
queue.append(7)
# [3,8,9,7]
print(queue)

