# 구현
# 입력
x, y = map(str, input())
alphabet = ["a","b","c","d","e","f","g","h"]
start_x = alphabet.index(x) + 1
start_y = int(y)
start = [start_x, start_y]
# 초기 이동 경우의 수
move_type = [(-2,-1), (-2,1), (2,1), (2,-1),
(1,2), (1,-2), (-1,2), (-1,-2)]
# 시뮬레이션 시작
count = 0
# 이동의 경우의 수를 순차적으로 넣어서
for move_x, move_y in move_type:
  copy_start = start.copy()
  nx = copy_start[0] + move_x
  ny = copy_start[1] + move_y
  # 이동이 가능한 경우 count에 1을 더함
  if nx > 0 and ny > 0 and nx <= 8 and ny <= 8:
    count += 1
print(count)