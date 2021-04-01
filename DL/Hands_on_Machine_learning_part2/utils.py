import numpy as np

def standard_scaling(x:"2D np.array"):
    """
    desc:
        전달인자(argument)를 정규화시키는 함수입니다.
    args:
        x:0번축은 데이터의 개수이고 1번축은 변수의 개수인 2차원이 넘파이 배열이 들어옵니다.
    return:
        각 변수별로 정규화가 되어진 값을 반환합니다.
    """
    return (x - x.mean(axis=0)) / x.std(axis=0)


def R_squared(pred_y:"2D np.array", true_y:"2D np.array"):
    """
    desc:
        회귀 예측 모델의 평가를 위한 지표인 결정계수를 계산하는 함수입니다.
    args:
        pred_y:예측값
        true_y:실제값
    return:
        전달인자를 받아 계산되어진 0~1 사이의 값을 가진 결정계
    """
    return 1 - ((np.square(true_y - pred_y)).sum() / (np.square(true_y - pred_y.mean())).sum())

def train_val_split(full_x, full_y, split_ratio = 0.8):
    """
    desc:
        전달인자를 훈련 데이터와 검증 데이터로 나누는 함수입니다.
        만들어 봤는데 기존 sklearn.model_selection 패키지의 메소드보다
        10배는 느리네요. 그냥 sklearn 쓰세요.
    args:
        full_x:입력 데이터
        full_y:출력 데이터
        split_ratio:전체 데이터에서 훈련 데이터의 비율
    return:
        훈련 데이터(입력), 훈련 데이터(출력), 검증 데이터(입력), 검증 데이터(출력)
    """
    # 범위 내 임의의 숫자 선택
    length = full_x.shape[0]
    train_number = round(length * split_ratio)
    random_index = np.random.choice(range(length), train_number)
    
    # 선택된 숫자 인덱스 불러오기
    x_train = full_x[np.isin(range(length), random_index)]
    y_train = full_y[np.isin(range(length), random_index)]
    x_val = full_x[np.isin(range(length), random_index, invert=True)]
    y_val = full_y[np.isin(range(length), random_index, invert=True)]
    return x_train, y_train, x_val, y_val
