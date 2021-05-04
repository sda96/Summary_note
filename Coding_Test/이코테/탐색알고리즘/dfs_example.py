adj_matrix = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9
# 시작점 v
def dfs(graph, v, visited):
  visited[v] = True
  # [2,3,8]속에서 하나씩 True인지 확인
  # graph[1] = [2,3,8]
  print(v, graph[v])
  # 하나의 탐색이 끝나면 다시 1로 돌아와 다른 길로 탐색 실시
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
    
print(dfs(adj_matrix, 1, visited))
