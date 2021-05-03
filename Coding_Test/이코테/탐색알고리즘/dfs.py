# Depth-First Search : 그래프에서 깊은 부분을 우선적으로 탐색
# 인접 행렬
INF = 999999999
graph = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
  ]
print(graph)
# 인접 리스트
graph = [[] for _ in range(3)]
# 노드0 에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))
# 노드1 에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0,7))
# 노드2 에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0,5))
print(graph)