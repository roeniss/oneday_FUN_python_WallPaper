from time import sleep 
from selenium import webdriver 
import random, os, ctypes
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
def todayWallpaper():
	print("Hello! Welcome to TODAY WALLPAPER!")
	print("카테고리 종류는 다음과 같습니다.\n\n[", end="")
	for k,v in CATEGORY.items():
		print("{}({}), ".format(v,k))
	while(1):
		num = input("어느 카테고리로 하시겠습니까? (숫자 입력) : ")
		if num.isdigit() and (int(num) in CATEGORY.keys()): 
			break
		else: 
			print("정상적인 숫자를 입력해주세요."	)	
	s = CATEGORY[int(num)]	
	print("\n진행중입니다. 잠시만 기다려주세요.\n")
	driver = webdriver.Chrome('C:/Users/user/Desktop/workbench/chromedriver.exe')

###---------------변경될 부분 START----------------###

	while(1):
		# "특정 페이지 접속--> 바탕화면 1개 선택 --> 해당 링크로 접속" 부분을 함수로 만들어서
		# 밖으로 빼냈습니다.
		searchPage(driver, s)
		# try 함수는 일단 실행을 해보고, 에러가 나면(=그런 값이 존재하지 않으면) except로 넘어갑니다. 문제가 없다면 곧바로 else로 갑니다.
		try:
			file = driver.find_element_by_css_selector("#wallpaper-resolutions").find_element_by_link_text('1920x1080')
		except:
			print("\n저런! 랜덤으로 찾아낸 배경화면에 {} 사이즈의 선택지가 없네요.\n 다시 검색해 볼게요.\n".format('1920x1080'))
			# 다시 한번 while()문의 처음으로 돌아가서, 검색을 시작하는 거죠.
			continue 
		else:
			# 여기까지 왔다면 try 부분을 잘 수행했다는 거고, 그건 자기 해상도에 맞는 링크가 있단 뜻이죠!
			file.click()
			break

###---------------변경될 부분 END----------------###

	filename = file.get_attribute('href').replace("http://wallpaperswide.com/download/","")
	fileAbsPath = "C:/Users/user/Downloads/" + filename
	while(True):
		if os.path.exists(fileAbsPath): 
			break
		else:	
			sleep(1) 
	driver.quit()
	ctypes.windll.user32.SystemParametersInfoW(20, 0, fileAbsPath , 3) 
	temp = input("설정이 완료되었습니다. 원본 이미지를 삭제할까요? (1:예 / 2:아니오) : ")
	if temp == "1":	
		os.remove(fileAbsPath)
		print("원본 이미지를 삭제했습니다.")
	else:
		print("원본 이미지를 보존합니다.")
	print("\n\n\n모든 작업이 종료되었습니다. 굿ㅡ 바이.\n\n\n")
	print("프로그램을 종료합니다.")
	sleep(1)

###---------------추가된 부분 START----------------###



def searchPage(driver, s):
	driver = driver # 앞쪽의 driver는 searchPage 함수 내의 변수고, 뒤쪽의 driver는 파라미터로 받아온 외부(= todayWallpaper 함수)의 driver입니다. 같은 driver라고 선언함으로써 이어주는 거죠. 쉽게말해 driver의 운전대를 저쪽 함수에서 이쪽 함수한테 넘겨준겁니다. 
	s = s # 마찬가지로, 앞쪽 s는 이 함수 내의 변수 이름이고, 뒤쪽 s는 바깥에서 가져온 함수입니다. 함수 이름 옆에(def searchPage) 인수로써 받아오고 있지요(driver, s).
	driver.get("http://wallpaperswide.com/" + s + "-desktop-wallpapers.html")
	images = driver.find_elements_by_css_selector('.thumb>a')

	# 랜덤으로 하나의 배경화면 선택(1페이지 내로 한정)
	image = random.choice(images)
	href = image.get_attribute("href")

	# 해당 배경화면의 상세설명 페이지로 이동
	driver.get(href)

###---------------추가된 부분 END----------------###


todayWallpaper() 