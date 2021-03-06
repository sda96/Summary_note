CRM기말과제
===========

#### 박창현

#### 2020 6 26

### kaggle cars데이터를 활용한 지도학습모델비교

목차
====

1.분석목적 및 데이터 구조

2.데이터 기초 분석

3.데이터 분석 방법

    3.1 데이터 분석 : 의사결정나무
    
    3.2 데이터 분석 : 다항 로지스틱 회귀분석
    
    3.3 데이터 분석 : 주성분 분석 + 다항 로지스틱 회귀분석
    
    3.4 데이터 분석 : 앙상블기법 랜덤 포레스트

4.결과요약

5.결론

6.분석의 한계

### 1.분석 목적 및 데이터 구조

해당 데이터는 kaggle에서 가져온 데이터로 변수brand의 범주에 따라서 데이터를 분류하는 연습문제 입니다. 해당 데이터를 4가지의 지도학습모델을 적용하여 올바르게 분류하고, 가장 정확도가 높게 나오는 모델을 찾고자 합니다.

    ## 'data.frame':    256 obs. of  8 variables:
    ##  $ mpg        : num  14 31.9 17 15 30.5 23 13 14 25.4 37.7 ...
    ##  $ cylinders  : int  8 4 8 8 4 8 8 8 5 4 ...
    ##  $ cubicinches: int  350 89 302 400 98 350 351 440 183 89 ...
    ##  $ hp         : int  165 71 140 150 63 125 158 215 77 62 ...
    ##  $ weightlbs  : int  4209 1925 3449 3761 2051 3900 4363 4312 3530 2050 ...
    ##  $ time.to.60 : int  12 14 11 10 17 17 13 9 20 17 ...
    ##  $ year       : int  1972 1980 1971 1971 1978 1980 1974 1971 1980 1982 ...
    ##  $ brand      : Factor w/ 3 levels " Europe."," Japan.",..: 3 1 3 3 3 3 3 3 1 2 ...
    ##  - attr(*, "na.action")= 'omit' Named int  15 34 41 173 181
    ##   ..- attr(*, "names")= chr  "15" "34" "41" "173" ...

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">변수명</th>
    <th class="tg-0pky">변수설명</th>
    <th class="tg-0pky">변수유형</th>
    <th class="tg-0pky">변수역할</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">mpg</td>
    <td class="tg-0pky">차량의 연비</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">cylinders</td>
    <td class="tg-0pky">엔지의 실린더 개수</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">cubicinches</td>
    <td class="tg-0pky">배기량(cc)</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">hp</td>
    <td class="tg-0pky">차량의 마력</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">weightlbs</td>
    <td class="tg-0pky">차량의 무게(파운드)</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">time.to.60</td>
    <td class="tg-0pky">차량의 속도</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">year</td>
    <td class="tg-0pky">차량이 만들어진 연도</td>
    <td class="tg-0pky">연속형 변수</td>
    <td class="tg-0pky">독립변수</td>
  </tr>
  <tr>
    <td class="tg-0pky">brand</td>
    <td class="tg-0pky">차량이 만들어진 브랜드</td>
    <td class="tg-0pky">범주형 변수</td>
    <td class="tg-0pky">종속변수</td>
  </tr>
</tbody>
</table>

데이터의 개수는 결측치를 제거한 256개이고, 변수의 개수는 8개인 데이터 구조 입니다. 모델을 만들때 사용하는 종속변수는 brand입니다. 종속변수인 brand의 범주는 총 3개로 US. , Japan. , Europe. 으로 나뉩니다.

### 2.데이터 기초 분석

<img src="https://imgur.com/qErzO0J.jpg">

    ## 
    ##  Europe.   Japan.      US. 
    ##       47       51      158

종속변수의 brand별 빈도수를 비교해본 결과 US. 가 158개로 가장 많았고 Europe.이 47개로 가장 적었습니다.

<img src="https://imgur.com/CwpHJw6.jpg">

x축을 hp로 하고 y축을 cubicinches로 하여 산점도로 나타낸 결과 US.의 경우 다른 범주에 비해서 hp와 cubicinches의 수치가 크게 나타나서 구분하기 쉬워 보입니다. 하지만, Japan과 Europe의 경우 두 범주를 구분하기는 어려울 정도로 서로 모여 있는 형태 입니다.

해당 산점도를 통하여 분류분석을 실시하였을 때 US.는 분류하기 쉽지만 다른 범주인 Japan.과 Europe.을 분류하기는 어려워 보입니다.

### 3.데이터 분석 방법

데이터 분류에서 의사결정나무와 다항 로지스틱 회귀분석, 주성분 분석을 실시한 다항 로지스틱 회귀분석, 랜덤포레스트 총 4가지 분석방법을 사용하여 그중에서 더 나은 정확도를 가진 모델을 찾으려고 합니다.

##### 3.1 데이터 분석 : 의사결정나무

의사결정나무란 데이터를 엔트로피 지수와 지니 지수와 같은 일정한 기준으로 분류하는 모델로 예측할 변수가 있는 지도학습 모델입니다. 의사결정나무는 데이터의 복잡도가 낮아지는 방향으로 분류를 하며 다른 모델에 비해서
정확도는 조금 떨어지는 편이지만 시각화를 했을때의 해석력이 좋기에 처음 데이터를 분류를 시작 할 때 참고하기 좋은 모델 입니다.

<img src="https://imgur.com/IKLFAnC.jpg">

의사결정나무는 제한을 걸지 않으면 끝노드의 데이터 불순도가 0이 될때 까지 분류하게 되는데 이는 너무 많은 종류의 끝노드를 만들게 되어 모델의 과적합을 유발하게 됩니다. 이를 막기 위하여 적절한 가지치기를 해야 합니다.

<img src="https://imgur.com/9SC7fFi.jpg">

    ## 
    ## Classification tree:
    ## rpart(formula = brand ~ ., data = data1, subset = train, method = "class", 
    ##     control = rpart.control(minsplit = 10))
    ## 
    ## Variables actually used in tree construction:
    ## [1] cubicinches cylinders   hp          mpg         weightlbs   year       
    ## 
    ## Root node error: 66/182 = 0.36264
    ## 
    ## n= 182 
    ## 
    ##         CP nsplit rel error  xerror     xstd
    ## 1 0.196970      0   1.00000 1.00000 0.098270
    ## 2 0.113636      2   0.60606 0.77273 0.091800
    ## 3 0.075758      4   0.37879 0.60606 0.084644
    ## 4 0.045455      5   0.30303 0.54545 0.081423
    ## 5 0.030303      6   0.25758 0.48485 0.077811
    ## 6 0.010000      8   0.19697 0.48485 0.077811

가지치기의 기준은 plotcp()함수를 활용하여 끝노드의 가중치가 cp값이 점선에 가까울수록 좋기 때문에. 위의 그래프의 경우에는 cp가 0.076을 사용하겠습니다.

<img src="https://imgur.com/SmDWiqn.jpg">

가지치기를 한 결과 이전 의사결정나무의 그래프보다 나뉘는 분류기준이 적게 나왔습니다.

    ##           pred
    ## y           Europe.  Japan.  US.
    ##    Europe.        5       7    4
    ##    Japan.         6      10    0
    ##    US.            4       7   31
    
    ## [1] 0.6216216

결과를 보니 이전 기초분석의 산점도를 통하여 보았던 내용과 같이 US.의 경우에는 cubicinches의 값이 171보다 크다는 분류기준으로 쉽게 나뉘지만 Japan과 Europe로 분류된 끝마디의 복잡도를 보니 두 범주를 나누는 명확한
기준을 찾기 어렵다는 것을 알 수 있었습니다. 의사결정나무로 검증형 데이터를 예측한 결과 그 정확도가 약 62%로 상당히 낮게 나왔습니다.

##### 3.2 데이터 분석 : 다항 로지스틱 회귀분석

다항 로지스틱 회귀분석은 종속변수가 2개이상의 범주를 가진 변수를 독립변수를 통하여 예측하는 회귀분석 입니다. 해당 데이터의 종속변수인 brand는 범주가 3개이기에 일반 로지스틱이 아닌 다항 로지스틱을 사용하였습니다.

    ##           pred
    ## y           Europe.  Japan.  US.
    ##    Europe.        6       4    6
    ##    Japan.         5      10    1
    ##    US.            4       5   33
    
    ## [1] 0.6621622

<img src="https://imgur.com/yiKppXC.jpg">

다항 로지스틱 회귀모델로 검증형 데이터를 예측한 결과 약 66%의 정확도가 나왔습니다. 이전 의사결정나무의 정확도인 62%보다는 높은 수치 이지만 수치의 차이가 생각보다 크지 않습니다. 이는 데이터 분석 방법에 문제가 있다고 생각하여 다른 방법을 적용해 보겠습니다.

##### 3.3 데이터 분석 : 주성분 분석 + 다항 로지스틱 회귀분석

<img src="https://imgur.com/B8AvX2r.jpg">

이전 다항 로지스틱 회귀분석을 진행하며 독립변수간의 상관성이 있을거라고 생각형하여 상관계수를 시각화한 결과 mpg는 year,time.to.60과는 양의 상관관계이고 weightlbs,hp,cubicinches,cylinders와는 음의 상관관계를 가집니다. 이를 통하여 독립변수간의 선형성은 존재하며 다중 공선성 문제가 발생한다는 것을 알 수 있었습니다.

    ## Standard deviations (1, .., p=7):
    ## [1] 862.3794148  41.9126315  16.2605515   4.8692777   2.3980031   1.6620788
    ## [7]   0.5211083
    ## 
    ## Rotation (n x k) = (7 x 7):
    ##                      PC1         PC2          PC3          PC4          PC5
    ## mpg          0.007535220 -0.02027576 -0.043226871 -0.844489616 -0.520021571
    ## cylinders   -0.001821078  0.01270159 -0.008984578  0.004471122  0.016547497
    ## cubicinches -0.118449432  0.93736934 -0.326869592 -0.011657175  0.005588920
    ## hp          -0.040834856  0.32134209  0.940343847 -0.063549807 -0.006580693
    ## weightlbs   -0.992087690 -0.12540707 -0.000158921 -0.003077852 -0.003694343
    ## time.to.60   0.001656317 -0.03395447 -0.075914902 -0.014414172 -0.190813066
    ## year         0.001192803 -0.02501412 -0.034602542 -0.531437286  0.832349645
    ##                      PC6           PC7
    ## mpg         -0.118481009 -0.0063762810
    ## cylinders   -0.049772502 -0.9984906199
    ## cubicinches  0.009078250  0.0146692306
    ## hp           0.081648954 -0.0087628050
    ## weightlbs   -0.003440582  0.0003120513
    ## time.to.60   0.976624292 -0.0516611661
    ## year         0.151423701  0.0038572660

<img src="https://imgur.com/I8kkkS7.jpg">

상관분석을 통하여 다중공선성 문제가 생긴다는 것을 알았으므로 비슷한 속성을 가진 독립변수끼리 묶어주는 차원축소 방법인 주성분 분석을 사용하겠습니다. 하게되면 PC2에서 그래프가 급격히 완만해지는 지점을 주성분 변수 개수를 사용 합니다. 그러므로 7개 독립변수가 아닌 2개의 주성분 변수를 사용하여 다항 로지스틱 회귀분석을 하겠습니다.

    ## # weights:  12 (6 variable)
    ## initial  value 199.947437 
    ## iter  10 value 94.365827
    ## iter  20 value 94.085281
    ## final  value 94.083276 
    ## converged
    
    ##           pred
    ## y           Europe.  Japan.  US.
    ##    Europe.        8       7    1
    ##    Japan.         5      10    1
    ##    US.            0       8   34
    
    ## [1] 0.7027027

<img src="https://imgur.com/tYvLh1w.jpg">

주성분 분석을 통하여 나온 주성분 변수 2개를 사용하여 다항 로지스틱 회귀분모델로 검증형 데이터를 예측한 결과 약 70%가 나왔습니다. 주성분 분석을 통하여 독립변수간의 다중공선성 문제를 해결하여서 이전의 모델보다 정확도가 약 4% 상승하게 되었습니다.

##### 3.4 데이터 분석 : 앙상블기법 랜덤포레스트

앙상블기법은 서로다른 파라미터로 나온 모델들의 결과를 취합하여 정확도가 높은 방향으로 만들어진 모델로 대표적으로 랜덤포레스트가 있습니다. 랜덤포레스트는 의사결정나무를 사용한 방법입니다.

<img src="https://imgur.com/6HTweSn.jpg">

현재 사용한 랜덤포레스트 모델은 500개의 의사결정나무를 만들고 변수의 중요도를 나타냈습니다. 해당 그림은 노드의 순수도를 기준으로 독립변수의 중요도를 나타낸 그림입니다. cubicinches가 종속변수 brand를 분류하는데 가장 중요한 변수입니다. 하지만 이외의 변수들의 중요도가 낮기 때문에 특정 범주밖에 분류를 못한다는 것을 알 수 가 있었습니다.

    ##           pred
    ## y           Europe.  Japan.  US.
    ##    Europe.       11       2    3
    ##    Japan.         5      11    0
    ##    US.            4       5   33
    
    ## [1] 0.7432432

<img src="https://imgur.com/DmmsWp3.jpg">

만들어진 랜덤포레스트 모델로 검증데이터를 예측한 결과 약 74%가 나왔습니다.

### 4.결과요약

  분석방법                                      정확도
--------------------------------------------- --------
  의사결정나무모델                              62%
  다항 로지스틱 회귀분석                        66%
  주성분 분석을 실시한 다항 로지스틱 회귀분석   70%
  랜덤포레스트                                  74%

총 256개의 cars데이터를 종속변수인 brand에 따라 분류를 하기위해서 4가지 분석방법을 사용하였습니다.

첫 번째로는 의사결정나무를 사용하여 시각화를 하였을때 무엇을 기준으로 분류하였는지 해석력이 좋았으나 3가지 방법중에서 가장 낮은 정확도인 62%가 나왔습니다.

두 번째 분석방법은 다항 로지스틱 회귀분석으로 의사결정나무 보다는 높은 정확도인 66%가 나왔습니다.

세 번째 분석방법은 다항 로지스틱 회귀분석을 하기전에 독립변수간의 다중공선성 문제를 고려하여 주성분 분석을 하여 나온 변수를 사용하여 다항 로지스틱 회귀분석을 실시한 결과 정확도가 70%가 나왔습니다.

네 번째 분석방법은 앙상블기법의 랜덤포레스트 모델을 통하여 7가지 독립변수중 cubicinches가 가장 중요한 변수였고 모델의 정확도는 74%가 나왔습니다.

### 5.결론

해당 분석의 목적은 데이터 분류의 해석력보다는 종속변수 brand의 3가지 범주를 정확하게 분류하는 정확도에 중점으로 분석을 하였기에 이 4가지 방법중에서 74%로 가장 정확도가 높은 방법인 앙상블 기법의 랜덤포레스트 모델을 사용하는 것이 합리적인 선택이라고 생각합니다.

### 6. 분석의 한계

1.적은 데이터 개수

cars데이터 자체의 개수가 모델을 학습시켜 정확도를 높이기에는 한계가 존재할 만큼 개수가 적은것이 아쉬웠습니다.

2.데이터의 불균형

기초분석에서의 종속변수의 범주별 빈도그림과 같이 US.의 경우가 다른 범주에 비해서 압도적으로 많아서 나머지 범주로 분류하기 어려웠습니다.

3.분석능력의 한계

기초분석의 산점도 그림을 통하여 US.의 경우 특징이 명확하여 모델이 분류하기 쉬웠지만 Europe.과 Japan.의 특징은 서로 구분할만 한 특징을 찾기 모호하기에 모든 모델에서 제대로 분류하지 못하였습니다.
