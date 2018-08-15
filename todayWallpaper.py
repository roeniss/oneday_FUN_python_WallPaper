import os, sys, random, ctypes
from time import sleep
from selenium import webdriver
import win32com.client as comctl
CATEGORY_NAMES = [
"Aero",
"Animals",
"Architecture",
"Army",
"Artistic",
"Black_and_White",
"Cartoons",
"Celebrities",
"Charity",
"City",
"Computers",
"Cute",
"Elements",
"Food_and_Drink",
"Funny",
"Games",
"Girls",
"Holidays",
"Love",
"Motors",
"Movies",
"Music",
"Nature",
"Seasons",
"Space",
"Sports", 
"Travel",
"Vintage",
]
CATEGORY = dict()
for k,v in enumerate(CATEGORY_NAMES):
	CATEGORY[k] = v 

def machine(size, downloadFolder):

	"""
	배경화면 변경기
	"""


	# 랜덤 확률로 발동
	start = False
	if random.randint(1,5) == 1: start = True
	# start = 1	
	if not start:
		wsh = comctl.Dispatch("WScript.Shell")
		wsh.SendKeys("%{F4}")

	# 인트로
	print("""\
                      .odMMMmysoo/shhyyyyyyyyyyyyy
                   `/dMNy/-      .-:yhyyyyyyssooo+
/++/:.             oMd/`          `--oy+//////////
mmmNMMNh/           :               .-oy//////////
    `.:+-                :+++hhs++/` `-+y/////////
                       :s-/oMNNMMy`s- `-oy//++++++
`::::-.               /o-dMNMo-.oNd`y- .-shsssssss
+/:./::++`           .y dMMMMMMmmMMy`h `-:msssssss
yNMhydh-`o/          // NMMNNMMm/omN`h  --hyssssss
MMMdo:-sm-o:         :o`MNssmMMmmhNy-s  `-+dssssss
MMMMMMMhMd`h          s/:mMMMMmMNs`/s`   -:myyssss
MMMMMMdo:s h           :++o/-::++++-``   .-hhyyyyy
s++NMMMMy-:o              .-::/-.----.   .-odyyyyy
mMMMmyh+`o+                `-------.`    .-odyyyyy
-///://++.                 .-..`` `      .-odyyyyy
::::...---`                              --ohyyyyy
.-----...`                              `--oyosyyy
.....```                                .--syoooos
                                        ---doooooo
                                       `--oyoooooo
                    -+yhmNMMMMNs       --+s/oooooo
                 .omMMMMMMMMMMMd      .-/y-.-+oooo
                -NMMMMMMMmhyso:      .-:h-....-/oo
                :yhdhyo:`           .-/h+.......:+
                                  `-:shsso-.......""")
	print("\"HOOOOOOLY SH*T! THIS IS AMAZING!!\".\n")
	sleep(1)
	print("[오늘의 배경화면 쇼쇼쇼]가 발동되었습니다.\n원하시는 카테고리를 골라주세요.\n")
	sleep(1)
	print("카테고리 종류는 다음과 같습니다.\n\n[", end="")
	for k,v in CATEGORY.items(): print("{}({}), ".format(v,k) ,end="")
	print("]\n")

	# 카테고리 설정 / 999 = random / s = selected Category
	while(1):
		num = input("어느 카테고리로 하시겠습니까? 999는 랜덤입니다. (숫자 입력) : ")
		if num.isdigit() and (int(num) in CATEGORY.keys() or int(num) == 999): break;
		else: print("정상적인 숫자를 입력해주세요."	)	
	try:
		s = CATEGORY[int(num)]
	except:
		s = CATEGORY[random.sample(CATEGORY.keys(),1)[0]]
	finally:
		print("\n진행중입니다. 잠시만 기다려주세요.\n")
	sleep(3)

	# 셀레니움 접속
	driver = webdriver.Chrome('chromedriver.exe') # C:/Users/user/Desktop/workbench/todayWallpaper/

	# 자기 해상도에 맞는 파일 다운로드
	while(1):
		searchPage(driver, s)
		try:
			file = driver.find_element_by_css_selector("#wallpaper-resolutions").find_element_by_link_text(size)
		except:
			print("\n저런! 랜덤으로 찾아낸 배경화면에 {} 사이즈의 선택지가 없네요.\n 다시 검색해 볼게요.\n".format(size))
			continue 
		else:
			file.click()
			break

	# 다운로드 할 파일의 이름을 캐치
	filename = file.get_attribute('href').replace("http://wallpaperswide.com/download/","")
	fileAbsPath = downloadFolder + filename

	# 파일 다운로드가 끝날 때까지 모니터링
	while(1):
		if os.path.exists(fileAbsPath): break
		else:	sleep(1)

	# 다운로드 완료되었으니 브라우저 종료
	driver.quit()

	# 배경화면으로 지정
	ctypes.windll.user32.SystemParametersInfoW(20, 0, fileAbsPath , 3) # SystemParametersInfoA

	# 원본 이미지 삭제
	temp = input("설정이 완료되었습니다. 원본 이미지를 삭제할까요? (1:예 / 2:아니오) : ")
	if temp == "1":	os.remove(fileAbsPath)

	# 아웃트로
	print("\n\n\n모든 작업이 종료되었습니다. 굿ㅡ 바이.\n\n\n")
	sleep(3)

	# cmd 종료
	wsh = comctl.Dispatch("WScript.Shell")
	wsh.SendKeys("%{F4}")

def searchPage(driver, s):
	driver = driver
	s = s
	driver.get("http://wallpaperswide.com/" + s + "-desktop-wallpapers.html")
	images = driver.find_elements_by_css_selector('.thumb>a')

	# 랜덤으로 하나의 배경화면 선택(1페이지 내로 한정)
	image = random.choice(images)
	href = image.get_attribute("href")

	# 해당 배경화면의 상세설명 페이지로 이동
	driver.get(href)

#실제 실행
machine(size="1920x1080", downloadFolder="C:/Users/user/Downloads/")
