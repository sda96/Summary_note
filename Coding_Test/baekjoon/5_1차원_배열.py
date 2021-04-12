N = int(input())
for i in range(N):
    case = list(map(int, input().split()))
    num = case[0]
    scores = case[1:]
    average = sum(scores)/len(scores)
    bucket = []
    for i in scores:
        if i > average:
            bucket += [True]
        else:
            bucket += [False]
    re = sum(bucket) / len(scores) * 100
    print("{:.3f}%".format(re))
