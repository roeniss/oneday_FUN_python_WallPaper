Oneday FUN Python - WallPaper part
===================================
원데이 FUN 파이썬 - 배경화면 편
------------------------------
> 모든 내용은 Windows 기준으로 작성하였습니다. Mac 등은 다른 식으로 접근해야 할 수도 있습니다.

# 1. 사전준비  
## 1-1. python3, pip 설치  
컴퓨터에 파이썬이 없다면 설치합니다.
[관련링크(제타위키)](https://zetawiki.com/wiki/%EC%9C%88%EB%8F%84%EC%9A%B0_Python_3_%EC%84%A4%EC%B9%98)  
해당 링크에서 **3번**(테스트)까지 해보시면 됩니다.
>pip는 python에 다양한 모듈을 추가할 수 있게 해줍니다. 편의점이라고 생각하시면 좋을 것 같아요.

## 1-2. Sublime text3 설치
직접 코드를 작성할 에디터를 설치합니다. 여기서는 서브라임 텍스트3를 사용하겠습니다.
[관련링크(네이버 블로그)](https://m.blog.naver.com/PostView.nhn?blogId=sprax&logNo=220636669357&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F).  
해당 링크에서 **6번, 7번은 제외하고** 완료해주시면 됩니다.  
> 꼭 이 에디터를 쓰실 필요는 없습니다. 본인이 쓰시는 에디터가 있으시다면 어느 것이라도 좋습니다.

## 1-3. Sublime text3 추가작업(한글 입력 개선, input 기능 추가)
Sublime text3를 사용하면 몇 가지 문제될 부분이 있기 때문에 추가 작업을 진행하겠습니다.
[관련링크(제타위키)](https://zetawiki.com/wiki/%EC%84%9C%EB%B8%8C%EB%9D%BC%EC%9E%84%ED%85%8D%EC%8A%A4%ED%8A%B8_IMESupport_%ED%8C%A8%ED%82%A4%EC%A7%80_%EC%84%A4%EC%B9%98)
> 위 링크 내용 중 \'**2 사전작업**\'은 이미 1-2에서 완료된 부분입니다(블로그 내 8~11번 항목).  


### (제타위키의 설명 중)"커맨드 팔레트를 열라는게 무슨 말이지?"  
라고 생각하시는 분도 있을 것 같아 스크린샷을 첨부합니다(3장).

(1) Sublime text3를 실행하시고,  


![1](https://user-images.githubusercontent.com/26613280/44080520-3efebadc-9fe7-11e8-8ccf-7f92dd0c6058.png)


(2) Ctrl+Shift+P 를 누르시면 이 창이 나옵니다. 엔터를 눌러주세요. (살짝 딜레이 있음)


![2](https://user-images.githubusercontent.com/26613280/44080521-3f2578e8-9fe7-11e8-9f27-4aa58c092c5a.png)


(3) 새로 나온 팝업창에 pci를 입력하시면 이 항목이 나옵니다(엔터).   


![3](https://user-images.githubusercontent.com/26613280/44080522-3f4a1ee6-9fe7-11e8-8cf8-7c2a98a2e9c5.png)


같은 방식으로, **sublimeREPL** 패키지도 설치해주세요! 약간 불안하신 분은 [관련링크(깃헙 블로그)](http://amazingguni.github.io/blog/2016/03/sublime-text%EB%A1%9C-python3-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0)의 상단 부분을 참고해주세요.

> 다른 패키지(추가기능)가 궁금하신 분들은 가볍게 [여기(네이버 블로그)](http://jos39.tistory.com/243)를 둘러보시길 바랍니다.


## 1-4. pip를 통한 패키지 설치(Selenium)
파이썬에 기능을 추가해주기 위해서, pip를 이용해 모듈을 하나 설치하겠습니다.  
Selenium : 크롬을 통해 인터넷에 접속하게 도와줍니다. [관련 링크(티스토리 블로그)](http://shaeod.tistory.com/915)  

## 1-5. 마지막으로, Chrome Driver 설치  
파이썬으로 Selenium 기능을 이용해서 인터넷에 접속할 때는, **특별한 크롬** 파일을 사용합니다.  
자신의 OS에 맞는(윈도우/맥/리눅스) 파일을 골라서 받아주세요. [관련링크(공식 홈페이지)](https://chromedriver.storage.googleapis.com/index.html?path=2.41/)



# 2. 이 강좌에서 배울 수 있는 것들


대략 다음과 같은 것들을 배웁니다. 빈 줄 빼고 대략 100줄 정도 되는 코드입니다.


1. 웹 크롤링(import Selenium)
2. 웹 페이지의 구성 요소의 이해(HTML, CSS)
3. 실제 폴더를 파이썬으로 접속(import os)
4. 파이썬을 이용하여 배경화면 설정(import ctypes)
5. 노트북 부팅될 때 실행되게 만들기(윈도우 작업 스케줄러)

(아마 프로그래밍을 하시는 분들은 여기까지만 보셔도 어렵지 않다는 걸 아시겠지요 😊)



# 3. 파일 소개


**commit 제목**(ex. "강의자료(알고리즘 v1.0)")을 누르시면 이 파일에 대한 설명을,  
**file 이름**(ex. "todayWallpaper.py")을 누르시면 실제 코드 내용을 보실 수 있습니다.


1. README.md - 지금 보고 계신 설명서입니다.
2. todayWallpaper(v1.0).py - 실제로 강의할 주 자료입니다. 더블샾(##)이 코드 부분이고 나머진 진짜 설명(주석)입니다.
3. todayWallpaper(v1.0s).py - 주석을 다 빼고, 부차적인 부분들(print나 sleep 등)을 빼고난 순수한 실행코드입니다. 압축버전이라고 말할 수 있겠군요.
4 .todayWallpaper(v1.1).py - 카테고리 분류 기능을 추가한 버전입니다.
5. todayWallpaper(v1.2).py - 매 부팅 때마다 실행되지'는' 않도록 수정한 버전입니다.
6. todayWallpaper.py - 제가 기존에 쓰던 버전입니다. 강의 때 설명하겠지만, 여기있는 것 중 강의하지 않는 것도 있고 강의 때보다 안좋은(더 귀찮고 쓸모없는) 코드들도 섞여있습니다. 
