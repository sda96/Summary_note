# Bitcoin : A Peer-to-Peer Electronic Cash System

### Abstract

purely [피어 네트워크](https://ko.wikipedia.org/wiki/P2P) 전자상거래는 한 집단이 다른 집단으로 어떠한 금융협회 없이 바로 온라인 결제를 보낼 수 있습니다. 

디지털 신호는 해결방법의 일부를 제공합니다, 하지만 주요 이점은 여전히 믿음직스러운 제 3삼자에게 이중-지불을 예방하기 위해서 요구되어지는 것이 없다는 것 입니다. 

우리는 피어 네트워크를 사용한 이중-지불 문제 해결법을 제안하겠습니다. 

이 네트워크는 주기적인 [해시](https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/) 기반 작업증명시스템으로 해싱 된 체인인 거래를 [타임스탬프](http://wiki.hash.kr/index.php/%ED%83%80%EC%9E%84%EC%8A%A4%ED%83%AC%ED%94%84)에 표시합니다. 

형성된 기록은 작업증명을 다시하지 않는 이상 바꿀수 없습니다. 

가장 긴 체인은 일련의 사건을 목격한 증거로써 제공될 뿐만 아니라, 이 작업은 가장 큰 cpu 출력으로부터 왔다는 증거이기도 합니다. 

주요 cpu 파워가 네트워크를 공격하기 위해 협동하지 않는 노드들에 의해서 조절되어지는 한, 그들은 가장 큰 체인을 형성하고 공격자들을 앞지를겁니다. 
네트워크 자체는 최소한의 구조를 요구합니다. 

메세지들은 가능한 멀리 퍼집니다. 그리고 노드들은 의식적으로 네트워크를 끊거나 재결합할수 있고, 가장 큰 작업증명 체인은 노드들이 없는 동안 발생했던 것의 증거로써 받아들여 집니다.

### Introduction

인터넷 전자상거래는 금융협회가 제공하는 믿음직한 3자는 전자 지불 처리를 하기 위해서 거의 의존해 왔습니다. 

대부분의 거래에서는 시스템이 잘 작동하는 반면에, 믿음에 기반한 모델이라는 선천적 약점에 의해서 여전히 고통을 겪고 있습니다.

완전한 비가역적인 거래는 실제로 불가능합니다, 왜냐하면 금융협회는 분쟁조정를 피할수 없기 때문입니다.

조정 비용은 거래 비용을 증가시켰고. 최소한의 실질적인 거래의 크기에 제한을 두었고, 작고 우연한 거래의 가능성을 쳐냈고, 그리고 비가역적(non-reversible) 서비스를 만드는 비가역적 지불을 만들기 위한 능력의 손실은 광범위한 비용이 듭니다.

반대의 가능성과 함께, 신뢰의 확산이 필요합니다. 

상인들은 그들의 고객들을 경계해야만 하고, 그들이 필요한 것 이상의 정보를 더 얻기위해서 고객들을 괴롭힙니다.

사기의 특정 부분은 피할 수 없이 받아들여집니다.

이러한 비용들과 지불의 불확실성은 개인이 물질적 화폐를 사용하는데 꺼려질 수 있습니다.

하지만 신뢰하는 집단없이는 지불을 만들기 위한 소통의 구조가 존재하지 않습니다.

신뢰를 대신할 암호화 증명 기반의 전자 지불 시스템에서 특정한 의지를 가진 두 집단이 직접적으로 서로 거래를 하는데 신뢰도 있는 제3삼자 없이 거래가 가능하려면 무엇이 필요할까요.

계산상으로 되돌릴 수 없는 거래는 사기로부터 판매자들을 지켜주고, 주기적인 조건부 날인 증서 구조는 구매자들을 지키기 위해서 쉽게 실행되어 질 수 있습니다.

이 논문에서는, 우리는 이중 지불 문제를 계산상의 증거가 연대기적 순서로 거래가 발생하는 P2P 분산형 타임스탬프 서버를 사용한 해결책을 제안합니다.

이 시스템은 정직한 노드가 침입하는 노드 그룹보다 더 많은 CPU 성능을 제어하는 한 안전합니다.

### Transactions

우리는 가상코인을 디지털 신호의 체인으로 정의합니다. 

각 소유자는 코인을 이전 거래, 다음 소유자의 공유키들을 말미에 추가한 해시에 디지털 서명을 함으로써 다음사람에게 전달합니다.

구매자는 소유권 체인을 검증하기 위해서 서명을 확인할 수 있습니다.