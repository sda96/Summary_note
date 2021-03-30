def standard_scaling(x: "2D numpy array"):
    """
    args:
        x : 0번축은 데이터의 개수이고 1번축은 변수의 개수인 2차원이 넘파이 배열이 들어옵니다.
    return:
        각 변수별로 정규화가 되어진 값을 반환합니다.
    """
    return (x - x.mean(axis=0)) / x.std(axis=0)
