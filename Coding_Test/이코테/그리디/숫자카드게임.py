# 그리디
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 뽑는 게임

# 입력
n, m = map(int, input().split())
result = 0
# 입력되는 배열중에서 작은 값을 고르고 이전까지 배열중에서 가장 큰값을 구함
for i in range(n):
  arr = list(map(int, input().split()))
  min_value = min(arr)
  result = max(result, min_value)
print(result)