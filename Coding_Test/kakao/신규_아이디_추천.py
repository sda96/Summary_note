s = "=.="

import re

def solution(s):
  s = s.lower()
  s = re.sub("[^a-z0-9-_.]","", s)
  s = re.sub("[..]+",".", s)
  s = re.sub("^[.]|[.]$","",s)
  if not s:
    s = "a"
  if len(s) >= 16:
    s = s[:15]
  s = re.sub("[.]$","",s)
  if len(s) <= 2:
    while True:
      s += s[-1]
      if len(s) == 3:
        break
  return s

print(solution(s))