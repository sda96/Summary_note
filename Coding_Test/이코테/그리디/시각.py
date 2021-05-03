# 완전탐색
# 전체 데이터 개수가 100만개 이하일 때 사용이 적절함
n = int(input())
count = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if "3" in str(h) + str(m) + str(s):
        count += 1
print(count)