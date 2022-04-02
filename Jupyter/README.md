conda env list <- 현재 사용가능한 커널명과 위치 출력  
conda info --envs <- 현재 사용가능한 커널명과 위치 출력  
- conda create -n [환경명] python=3.8 numpy=1.19.0<- 파이썬3.8 버전의 환경명을 가진 가상환경 생성  
- pip install ipykernel <- 커널패키지 다운로드  
- python -m ipykernel install --user --name [환경명] --display-name [커널명] <- 커널 생성  
- conda activate [환경명]  
    - conda deactivate 
    - jupyter kernelspec list <- 생성된 커널 확인
    - jupyter kernelspec uninstall [커널명] <- 커널 삭제
    - conda env remove -n [환경명] <- 가상환경 삭제
- conda install [패키지명]=[버전] -n [환경명] <- 특정 가상환경에 특정 패키지 설치
    - conda list <- 설치된 패키지 리스트
    - conda search <- 설치된 패키지 조회
    - conda remove [패키지명] <- 설치된 패키지 삭제
    - conda clean --all <- 캐시삭제 ./Anaconda3/pkgs에 있는 것들 삭제

커널연결오류
[IPKernelApp] ERROR | Failed to load connection file:
ImportError: DLL load failed while importing win32api: 지정된 모듈을 찾을 수 없습니다.
위의 에러 발생시 conda install pywin32 -n [환경명] 로 해결

fatal error C1083: Cannot open include file: 'zmq.h': No such file or directory
pip install pyzmq


pip은 파이썬의 패키지 관리자 입니다.
pip install -r requirements.txt

콘다 가상환경에서 idle를 여는 방법입니다.
activate myenv
python -m idlelib

콘다 가상환경에서 파이썬 버전 바꾸기
conda activate my_env
conda install python=3.6

가상환경은 패키지 관리에 용이한 방법입니다.

아나콘다는 데이터 과학, 머신러닝에 필요한 패키지들이 설치되어있는 도구로 
가상환경이 제공하는 기능을 가지고 있습니다.


참고자료
https://data-newbie.tistory.com/113
https://docs.conda.io/projects/conda/en/latest/commands.html
(window 단축키 임의지정 doskey ls = dir)[https://somjang.tistory.com/entry/Windows-%EB%AA%85%EB%A0%B9-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8cmd%EC%97%90%EC%84%9C-ls-clear-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95]
