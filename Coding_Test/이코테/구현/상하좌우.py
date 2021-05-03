# 구현 문제
# 입력
n = int(input())
arr = list(map(str, input().split()))
# 초기 조건
# 움직이는 경우의 수 미리 지정
move_type = ["L","R","U","D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 초기 시작 조건 지정
start = [1, 1]

# 입력값에 맞게 시작점에서 다음 위치를 찾음.
for move in arr:
  index = move_type.index(move)
  # x좌표의 다음 위치
  nx = start[0] + dx[index]
  # y좌표의 다음 위치
  ny = start[1] + dy[index]
  # 이동을 하기 전에 값이 0보다 크고 n보다 작은지 확인.
  if (nx > 0 and ny > 0) and (nx <= n and ny <= n):
    # 조건에 맞으면 이동한 시작점으로 새로 저장.
    start[0] = nx
    start[1] = ny
  print(start)

