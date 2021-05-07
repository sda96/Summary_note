from collections import Counter
s = "aabbaccc"

def split_s(length):
  split = [i for i in range(0, len(s), length)]
  bucket_split_s = []
  for k in split:
    bucket_split_s += [s[k:k+length]]
  return bucket_split_s



split_list = split_s(1)

start = split_list[0]
k = 0
a = []
for j in split_list:
  print(j)