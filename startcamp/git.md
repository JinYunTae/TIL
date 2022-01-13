## Git

### Git을 이용하는 이유

* Git을 이용한 버전관리

버전 : 컴퓨터 소프트웨어의 특정 상태

관리 : 어떤 일의 사무, 시설이나 물건의 유지, 개량

프로그램 : 

찐막 - 찐찐막 - 최종 - 진짜 최종 ... (어느게 진짜 최종이지?) => 날짜를 붙여 정리 (뭘 수정했지?) => 변경사항을 기록하는 파일을 따로 만들기(용량이...) => 중간 수정 레포트들은 변경사항만 남기자(이전 시점 파일이 필요하면?) => 최종본부터 역으로 취소하면서 되짚기

이것이 버전 관리 프로그램의 메인컨셉

그러나 얘도 못하는게 있다! - 수정한 이유에 대해서는 알 수 없음, 따로 기록해 줘야함! -> 인수인계, 문서로써의 소통 굿



__분산__ 버전 관리 프로그램

중앙집중식 버전관리 - 변경 이력을 중앙이 관리, 개별 사용자는 접속해서 확인 => 저장소가  터지면 끝

분산 버전 관리 - 변경 이력을 모두가 가지고 있음 => 한 곳이 잘못되도 다른 사용자 보유 정보로 복구 가능

**프로그래머는 불이나면 데이터를 깃에 푸시하고 탈출한다**

버전관리 = 컴퓨터 소프트웨어의 특정 상태를 관리하는 것



* Github을 이용한 포트폴리오

지금까지 해온 흔적으로 사람을 판단할 수 밖에 없음 - 그 흔적을 github에 남긴다

github - TIL (Today I Learned) 파일 관리(면접, 서류통과 용)

gitlab - 과제제출로 이용할 예정

1 project - 1 repository 국룰, 매일 매일 오늘 배운거 typora에 정리해서 github으로!

SSAFY(SSAFY, 싸피 단어 포함) 자료는 **절대** Github **public**에 올리지 말것! **보안서약** 준수!

ㄴ **Private**에 올릴것!

관통프로젝트 자료 업로드 시 주의! - 만약 연락 받는다면 무조건 내리거나 개인 전환

GitBash에서 TIL 폴더 git연동

TIL 폴더에서 우클릭 => gitbash 열기 => bash에서 `git init`입력



git의 3가지 공간

로컬 저장소 (내 컴퓨터)

​	working directory(작업공간) - Staging Area - Local Repository

​	ㄴStaging Area - 업로드 전 확인/검수하는 공간 (불필요한게 있나? 빠진건 없나?)

Working directory : 실제 폴더를 참조해 변화된 내용이 있는 파일만 가져옴

working directory => Staging Area : git add

Staging Area => Local Repository : git commit => ver1 생성

변경사항 발생 => Working directory가 참조 => Staging Area에서 검수 => Local Repository => ver2 생성 및 git은 이제 ver2 참조