from time import sleep # sleep(second) : sleep(1) = 1초 대기
from selenium import webdriver # 크롬을 파이썬으로 조종할 수 있어요
import random # 무언가(?)를 랜덤으로 할 수 있어요. 랜덤으로 숫자를 만들어주거나, 리스트에서 랜덤으로 항목을 뽑아줘요.
import os # 탐색기를 키는 것처럼, 컴퓨터의 파일들을 조작할 수 있어요.
import ctypes # 파이썬으로 C언어에서 하는 기능들을 쓰게 한다는데, 핵심은 바탕화면 설정 기능을 담고 있다는 점이예요.
import win32com.client as comctl # 윈도우 프로그램들을 조작할 수 있어요.

def todayWallpaper():
	print("Hello! Welcome to TODAY WALLPAPER!")
	## sleep(1)

	# webdriver.Chrome(chrome_file_path) >> 이제부터 chromedriver.exe을 실행할거야(새 크롬창이 열림)
	# driver >> 그리고 그 크롬의 운전대를 driver라는 변수에 줄거야(driver에 각종 메소르를 사용해서 크롬창을 조종할 수 있음)
	# "driver =" 부분을 통째로 지워도 실행은 돼요. 하지만 운전대 변수를 선언하지 않았으니 조종할 수가 없겠죠?
	## print("크롬 드라이버를 실행합니다.")
	## driver = webdriver.Chrome('C:/Users/user/Desktop/workbench/chromedriver.exe')
	## sleep(1)

	# get(site_name) : 해당 site 주소로 이동
	## print("http://wallpaperswide.com으로 이동합니다.")
	## driver.get("http://wallpaperswide.com/")
	## sleep(1)

	# find_elements_by_css_selector(css_selector) : 웹 페이지의 요소 중 특정 요소(element)를 잡아낼건데, 잡아낼 때 css 셀렉터를 통해 골라낼 것임
	# 그리고 골라낸 요소들을 images라는 변수에 넣을 것임
	# 이 타이밍에 css가 무엇인지 설명해볼게요.
	## print('배경화면 리스트를 추출합니다.')
	## images = driver.find_elements_by_css_selector('.thumb>a')

	# 아래 코드로 방금 뽑아낸 따끈따끈한 element들을 구경할 수 있어요
	## for each in images:
	## 	print(each,"\n\n")

	# 하지만 위 코드는 별로 이쁘지 않아요. 왜냐면 element들은 다양한 내용을 가지고 있기 때문에 정확히 뭘 보고 싶은건지 지정을 안해주면 element 각각의 고유번호만 알려주거든요. 이렇게 한 번 해볼까요?
	## for each in images:
	## 	print(each.get_attribute('outerHTML'),"\n")

	# "아니, 근데 가만히 보니까 항목이 9개네요? 사진은 10장인데?"
	# 사실 왼쪽 맨 위 사진은 조금 다른 구조를 가지고 있습니다. 그래서 따로 추가를 해줘야되는데, 복잡하니까 그냥 나머지 9개만 가지고 설명할게요 :)

	# choice(list) : list 내의 아이템 중 하나를 랜덤으로 고릅니다
	## print('배경화면 리스트 중 하나를 무작위로 선택합니다.')
	## image = random.choice(images)
	# 그 항목에서 주소를 의미하는 href(hypertext reference)의 값을 location이라는 변수에 저장합니다. 이제 어디로 가야할 지 알았어요!
	## location = image.get_attribute("href")
	# 해당 주소로 이동합니다.
	## print(location,"으로 이동합니다.")
	## driver.get(location)
	
	# find_element_by_link_text(text) : 링크에 적힌 텍스트를 보고 특정 element를 골라내기
	# text 칸에 자신의 바탕화면 사이즈를 적어봅시다('가로x세로'의 형태! 따옴표까지!)
	# 주의!! 자신 모니터 해상도에 맞는 링크가 없을 경우 에러가 발생할 수 있습니다. 로그창(Ctrl+B 누르면 나오는 창)을 잘 확인해주세요!
	## print("모니터 해상도에 맞는 파일을 다운로드 하고 있습니다.")
	## file = driver.find_element_by_link_text('1920x1080')
	## file.click()
	# (이 쯤에서 사람들이 잘 따라오고 있는지 확인할 것)

	# 다운로드가 다 되었는지 확인하는 방법 1 : 적당히 넉넉하게 대기한다
	## print("설치가 완료될 때까지 대기중입니다.")
	## sleep(10)
	# 다운로드가 다 되었는지 확인하는 방법 2 : 파일의 이름을 확인한 뒤, 다운로드 폴더에 그 파일이 있는지 계속 감시한다 >> better way!

	# 먼저 다운로드하는 파일 이름 알아내는 법은 다음과 같아요
	# replace(old, new) : old라는 글자는 전부 new로 바꾼다
	# file.get_attribute('href') = "http://wallpaperswide.com/download/배경화면-이름-wallpaper-가로x세로.jpg"
	## filename = file.get_attribute('href').replace("http://wallpaperswide.com/download/","")
	# filename에 다운받을 파일 이름만 남았는지 확인해보아요
	## print("다운받고 있는 파일의 이름은",filename,"입니다.")
	# 이제 filename과 같은 이름을 가진 파일이 "다운로드 폴더"에 존재하는지 지켜봅시다.
	# 너무 짧은 간격으로 계속 관찰하면 컴퓨터가 아파합니다. 적당히 1초에 한번씩만 봅시다.
	# 먼저 다운로드 폴더랑 파일명을 합쳐주어야 해요. 탐색기 상단 부분을 클릭하면 실제 주소를 알 수 있어요.
	## fileAbsPath = "C:/Users/user/Downloads/" + filename
	## print("다운로드 중인 파일의 절대경로는",fileAbsPath,"입니다.")
	# fileAbsPath는 이런식으로 표시됩니다 : "C:/Users/user/Download/아까-받은-바탕화면-이름-wallpaper-가로x세로.jpg"
	# os.path는 컴퓨터의 파일을 건드릴 수 있는 모듈이예요.
	## print("다운로드가 완료될 때까지 다운로드 폴더를 감시합니다.")
	## while(True):
	## 	if os.path.exists(fileAbsPath): # 파이썬에서는 "if a == True:"와 "if a:"가 같습니다!
	## 		break
	## 	else:	
	## 		print("아직 다운로드가 완료되지 않았습니다.")
	## 		sleep(1) # << 이 부분은 없어도 돼요. 그러면 '최고속도로' while문을 반복하는거죠..

	# 크롬 종료는 이쪽이라구!
	## print("크롬 드라이버를 종료합니다.")
	## driver.quit()


	# 여기서부턴 좀 수월할 겁니다... 이제 Selenium과 Chrome은 안녕!
	# ctypes.windll.user32.SystemParametersInfoW(20, 0, 파일절대경로 , 3) : 바탕화면을 변경합니다. 왜 코드가 이러냐구요? 글쎄요... 저도 검색해서 찾았을 뿐...
	# 이런 부분에서 원리를 이해하는건 시간낭비라고 생각했습니다(변명).
	## print("다운받은 파일을 바탕화면 이미지로 설정합니다.")
	## ctypes.windll.user32.SystemParametersInfoW(20, 0, fileAbsPath , 3) 
	# 만약 재부팅후 바탕화면이 사라졌다면... SystemParametersInfoW 대신 SystemParametersInfoA 를 써보세요!

	# 지저분한 원본파일을 지웁시다. 하지만 다운받은 배경화면이 너무 이쁠 수 있으므로 한 번 물어보도록 합시다
	# remove(file) : 해당 파일 삭제. 경로까지 정확히 지정해 줍시다.
	## temp = input("설정이 완료되었습니다. 원본 이미지를 삭제할까요? (1:예 / 2:아니오) : ")
	## if temp == "1":	
	## 	os.remove(fileAbsPath)
	## 	print("원본 이미지를 삭제했습니다.")
	## else:
	## 	print("원본 이미지를 보존합니다.")

	# 자, 모든 작업이 끝났어요!
	## print("\n\n\n모든 작업이 종료되었습니다. 굿ㅡ 바이.\n\n\n")
	## sleep()을 넣는 이유는, 위 마무리 멘트를 읽을 시간은 줘야되니까요. 안그러면 굿ㅡ 바이 가 표시되는 순간 프로그램이 종료될 거예요. 8ㅅ8
	## sleep(1)
	## print("3.....")
	## sleep(1)
	## print("2.....")
	## sleep(1)
	## print("1.....")
	## sleep(1)
	## print("프로그램을 종료합니다.")
	## sleep(1)


	# 여기까지 했으면 자동으로 시작되고 프로그램이 종료되게 해볼까요?
	# cmd를 배울 차례입니다.


todayWallpaper() 