[→ Open in Slid](https://slid.cc/vdocs/81b732785531497986986325932cde99)


---


mac : iterm2


window : cmder

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/7403204e-f03f-40eb-bc82-ee92c3b32624.png "git 배우기 image")

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/8c9ff947-594a-4a8e-ae75-b4e26c9fe601.png "git 배우기 image")


core.autocrlf는 window면 true로 mac이면 input 명령어를 추가합니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_markup_images/81b732785531497986986325932cde99/7cccba73-5fde-4de2-aed4-4fcdb5e429ee.png "git 배우기 image")


core.autocrlf를 사용하는 이유는 각 os마다 사용하는 줄바꿈을 할 때 사용되는 문자열이 다르기 때문




![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/7cb4b09c-6f1a-4ce8-a51a-d4dc9a83050c.png "git 배우기 image")


git init으로 git project를 시작하면 .git이라는 숨김폴더가 생깁니다.


rm -rf는 단순히 폴더를 삭제하는 터미널 명령어 입니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/f3d525f2-19d0-4ca1-8e1a-75df1a4ed57f.png "git 배우기 image")


git status는 현재 staging area와 git repository의 상태를 보여주는 명령어 입니다.


git config --global alias.st status는 git st 명령어를 입력시 git status가 자동완성이 되는 기능을 해줍니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/5e2bf92f-c93e-475a-95ca-ffc91bfb4f8c.png "git 배우기 image")


git은 위와 같은 3가지의 작업환경이 존재합니다.


사용자가 작업하는 공간 : working directory


버전 히스토리를 저장할 준비를 하는 공간 : staging area


버전의 히스토리를 가지고 있는 공간 : git directory(repository)

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_markup_images/81b732785531497986986325932cde99/fd45a90f-505a-449c-9ec7-98784799a11f.png "git 배우기 image")


git commit으로 준비가된 파일을 repository에 넣습니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/e1b54a96-c960-47b3-b77f-43a7714a9d0b.png "git 배우기 image")


git checkout으로 다시 전환 가능

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/d2a8de98-97f9-4943-af55-66858ad339b8.png "git 배우기 image")


repository에서 github로 업로드

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/17a26e97-1fa0-4191-809c-a0fe1fc08dcc.png "git 배우기 image")


github에서 repositoy로 업데이트

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/20d95034-5c7f-48cb-ae0a-390d5803c826.png "git 배우기 image")


각 파일에는 고유한 hash code가 부여됩니다. 해당 코드는 id, 버전 메시지, 작성자, 날짜와 시간등이 저장되어 버전 정보를 참조할 수가 있습니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/66485f26-f02a-4a0a-8eaa-964b471064d4.png "git 배우기 image")


untracked : .git으로 흔적이포함된 파일들


tracked : 새로 만들어진 파일, git init으로 초기화가되어 .git에 포함되어지지 않은 파일들

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/0b277bd7-70fa-4a61-a0f7-d9b25ce1d86e.png "git 배우기 image")


추적중인 파일중에서 수정이된 파일을 modified 안된 파일을 unmodified라고 부릅니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/fdaeaf94-0e47-4ad5-944f-86d85c27cd16.png "git 배우기 image")


수정이된 파일만 staging area로 갑니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_markup_images/81b732785531497986986325932cde99/d0b0b4f1-4568-4d73-a6a1-754c854344fd.png "git 배우기 image")


git add를 이용하여 로컬 환경에서 staging area에 올립니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/f83f6052-c4bd-469c-a7ef-66a38b75d393.png "git 배우기 image")


git rm --cached *을 사용하면 staging area에 있던 모든 파일을 취소할 수 있다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/6fc70ed6-cbe2-46e9-b86a-d268693c1080.png "git 배우기 image")


tracking 하고 싶지 않은 파일은 .gitignore에 적으면 무시가 됩니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/b2ce92f6-8a92-4d1b-9f4c-a41e1fc7deaa.png "git 배우기 image")


.gitignore은 이런식으로 사용하면 됩니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/c8f62048-6070-45a1-a6a7-bf8a55c67167.png "git 배우기 image")

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/1771a864-7c77-4049-9f41-7641ff6a93fe.png "git 배우기 image")


git diff는 어떤 파일의 내용이 수정되었는지 확인하는 명령어 입니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/dae497ce-074d-472a-8fad-c93b99c56abc.png "git 배우기 image")


-1은 이전에 있던 내용이고


+1, 2는 추가된 내용이 있는데 2번째 줄까지 확인하라는 뜻으로 +초록색은 추가된 내용 -빨간색은 제거된 내용


q를 눌러서 종료

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/f5207c10-dac3-421f-ae92-2cc7d98ca8ba.png "git 배우기 image")


staging area에 있는 내용들 확인 --cached도 가능

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/849d92a8-aa88-4f6f-b6e5-ff46c833d314.png "git 배우기 image")


git commit을 하면 버전이 만들어집니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/f6b5e18b-e2b5-409e-9ce6-56f6df604ead.png "git 배우기 image")


상세설명사항도 추가됨

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/8f1e5595-afbd-401f-ac7d-75f9a54967a7.png "git 배우기 image")


git log를 이용하여 commit 내용, 시간 등 알 수 잇음

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/1226d5e4-2863-4d94-9240-3ed29985f33f.png "git 배우기 image")


git commit -am "내용"이면 모든 내용을 add하고 바로 commit한다는 의미

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/81b732785531497986986325932cde99/4a6aaec9-512c-4b65-88c2-e5152c36167c.png "git 배우기 image")


.git directory는 버전의 과거 기록을 모두 저장하여 창고 같은 역할을 하고 있습니다.


어플리케이션을 세분화하여 작은 단위로 나누어서 history에 저장하는 것이 의미있습니다.&nbsp;


commit 내용에는 변경사항, 업무내용등을 추가하는 것이 좋습니다.


commit 내용에 맞는 행동만 추가하는게 좋습니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/image_upload/81b732785531497986986325932cde99/490f752a-75e5-4c52-833c-7ffe4199bd0e.png "git 배우기 image")


git log를 하면 commit들의 id가 나옵니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/image_upload/81b732785531497986986325932cde99/977efd93-e530-4445-9d35-e559c6b3ac40.png "git 배우기 image")


git checkout "commit id"를 하면 해당 commit으로 돌아가집니다.

![](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/image_upload/81b732785531497986986325932cde99/91ef3bb1-6a6f-4aef-827a-bac7fd39ad0b.png "git 배우기 image")


git checkout - 를 하면 이전 commit으로 돌아옵니다.


















