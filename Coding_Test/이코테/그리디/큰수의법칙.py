# 그리디
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만든다. 하지만 연속해서 k번 초과하여 더할수는 없는 없고 두 번째로 큰 값을 더한 뒤 다시 가장 큰 값을 더할 수 있음.
# 입력
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
# 배열 내에서 첫 번째, 두 번째 값 구하기
# 배열내의 원소를 오른차순으로 정렬
arr.sort()
# 첫 번째로 큰 값
first = arr[-1]
# 두 번째로 큰 값
second = arr[-2]


# k의 배수마다 second를 더하고 나머지는 first를 더함, 더하는 횟수는 m을 기준으로 더할 때마다 1씩 감소하여 0이되면 반복을 멈춤
result = 0
while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
    print(result)
  if m == 0:
    break
  result += second
  m -= 1
print(result)