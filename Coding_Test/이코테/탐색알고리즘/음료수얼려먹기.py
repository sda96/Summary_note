# 입력
n, m = map(int,input().split())
bucket_arr = []
# 2차원 리스트의 맵 정보 입력
for i in range(n):
  arr = list(map(int, input()))
  bucket_arr += [arr]
# dfs로 특정 노드 방문뒤 연결된 모든 노드 방문
def dfs(x, y):
  # 주어진 범위를 벗어나면 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않으면
  if bucket_arr[x][y] == 0:
    # 해당 노드 방문 처리
    bucket_arr[x][y] = 1
    # 상하좌우 위치 모두 재귀적 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False
# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현 위치에서 dfs 수행
    if dfs(i,j) == True:
      result +=1
# 결과 출력
print(result)