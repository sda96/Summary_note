# 입력
n, m = map(int, input().split())
start_x, start_y, direction = map(int, input().split())

# 지나간 자리 1로 채우고 나머지 자리는 0으로 만듬
back = [[0]*m for _ in range(n)]
back[start_y][start_x] = 1
# 북, 동, 남, 서
defense = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 맵 다운로드
bucket_matrix = []
for _ in range(n):
  matrix = list(map(int, input().split()))
  bucket_matrix += [matrix]
# 탐험 시작
# 다음 위치 탐색 후 이동 좌표 가져오기
# 조건에 맞는 경우 이동, 지나온 자리는 1로 채우기
