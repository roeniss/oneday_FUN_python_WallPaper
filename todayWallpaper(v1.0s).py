from time import sleep 
from selenium import webdriver 
import random, os, ctypes
import win32com.client as comctl

def todayWallpaper():
	print("Hello! Welcome to TODAY WALLPAPER!")
	driver = webdriver.Chrome('C:/Users/user/Desktop/workbench/chromedriver.exe')
	driver.get("http://wallpaperswide.com/")
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