from time import sleep 
from selenium import webdriver 
import random, os, ctypes
import win32com.client as comctl

###---------------추가된 부분 START----------------###
# v1.1에서는 해당 홈페이지의 각 카테고리를 직접 지정해보자!
# 각 카테고리의 이름을 리스트 형태로 모두 적어주고...(일일이 적은거 아님 엑셀에 복붙해서 가져옴 ㅎㅎ)
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
"Nature",i
"Seasons",
"Space",
"Sports",
"Travel",
"Vintage",
]

# 1,2,3,... 숫자를 입력하면 카테고리 이름이 나오도록 딕셔너리로 변환해줍니다.
# 왜 굳이 딕셔너리 형태를 쓰는 것인가? >> https://github.com/roeniss/oneday_FUN_python_WallPaper/issues/2 << 여기에 적어두었어요.
CATEGORY = dict()
for k,v in enumerate(CATEGORY_NAMES):
	CATEGORY[k] = v
###---------------추가된 부분 END----------------###

def todayWallpaper():
	print("Hello! Welcome to TODAY WALLPAPER!")

###---------------추가된 부분 START----------------###
	
	# 카테고리 소개
	print("카테고리 종류는 다음과 같습니다.\n\n[", end="")
	for k,v in CATEGORY.items(): # k = 숫자, v = 카테고리 영문명
		print("{}({}), ".format(v,k))

	# 제대로 된 숫자를 입력하면 while문을 벗어날 수 있음
	while(1):
		num = input("어느 카테고리로 하시겠습니까? (숫자 입력) : ")
		# 숫자인지 검사한 후 >> 카테고리의 숫자들(리스트 형태)에 포함되는 숫자인지를 판단합니다.
		if num.isdigit() and (int(num) in CATEGORY.keys()): 
			break
		else: 
			print("정상적인 숫자를 입력해주세요."	)	

	s = CATEGORY[int(num)] # 해당 숫자에 해당하는 카테고리 이름(영어)를 변수 s에 저장합니다.
	
	print("\n진행중입니다. 잠시만 기다려주세요.\n")
###---------------추가된 부분 END----------------###

	driver = webdriver.Chrome('C:/Users/user/Desktop/workbench/chromedriver.exe')

###---------------변경된 부분 START----------------###

	# 해당 세부 카테고리로 이동합니다.
	driver.get("http://wallpaperswide.com/" + s + "-desktop-wallpapers.html")
	
###---------------변경된 부분 START----------------###

	images = driver.find_elements_by_css_selector('.thumb>a')
	image = random.choice(images)
	location = image.get_attribute("href")
	driver.get(location)
	file = driver.find_element_by_link_text('1920x1080')
	file.click()
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

todayWallpaper() 