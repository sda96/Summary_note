from collections import deque
# 입력
n, m = map(int, input().split())
# 지도 입력
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
# 좌표 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs 소스코드 구현
def bfs(x, y):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y))
  # 큐가 빈 리스트가 될떄까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로 위치 
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[nx][ny] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(0,0))

