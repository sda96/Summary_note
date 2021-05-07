orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
result = ["AC", "ACDE", "BCFG", "CDE"]

from itertools import combinations
from collections import Counter




def solution(orders, course):
  bucket_combi = []
  for num in course:
    for order in orders:
      combi = list(combinations(order, num))
      combi = list(map(lambda x: "".join(list(x)), combi))
      bucket_combi += combi
  
  bucket_key = []
  count = Counter(bucket_combi).most_common()
  dic_count = dict(count)
  for num in course:
    case_key = [key for key, value in count if len(key) == num][0]
    bucket_key += [case_key]
    new_key = [key for key, value in count 
    if dic_count[case_key] == value 
    if len(key) == num]
    bucket_key += new_key

    
  return sorted(list(set(bucket_key)))
print(solution(orders,course))