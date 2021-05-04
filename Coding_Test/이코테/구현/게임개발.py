# 입력
n, m = map(int, input().split())
start_x, start_y, point = map(int, input().split())

bucket_arr = []
for i in range(n):
    arr = list(map(int, input().split()))
    bucket_arr += [arr]


# 시뮬레이션
def turn(number):
    if number == 0:
        return 3
    return number - 1

# 기본설정
direction = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
batch = [[False]*m for _ in range(n)]

# 지나간 자리 표시
batch[start_x][start_y] = True


# 지나간 자리 표시
batch[start_x][start_y] = True
footprint = []


# 4가지 방향 탐색
while True:
    for i in range(4):
        # 정해진 방향 1개 탐색
        new_point = turn(i)
        # 위치 이동 좌표 불러오기
        x, y = direction[new_point]
        # 새로운 이동 좌표 
        nx = start_x + x
        ny = start_y + y
        # 새로운 이동 좌표가 육지이고
        if bucket_arr[nx][ny] == 0:
            # 새로운 이동 좌표가 이전에 지나가지 않았다면
            if batch[nx][ny] == False:
                # 새로운 이동 좌표로 기존 좌표 이동
                batch[nx][ny] = True
                start_x = nx
                start_y = ny
            else:
                pass
        else:
            pass
    # 반복되는 흔적이 없으면 흔적을 기록합니다.
    if [start_x, start_y] not in footprint:
        footprint += [[start_x, start_y]]
    # 반복되는 흔적이 있으면 반복문을 멈춥니다.
    else:
        break

print(sum(sum(batch,[])))