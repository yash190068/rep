import undetected_chromedriver as uc
import time
import random
import threading
driver = uc.Chrome()

vlist = ['https://youtu.be/lUxzjQvNBmg','https://youtu.be/PHBLddvszao','https://youtu.be/uWcyQKQBnXk']
tabs = 4

def view(driver):
	for i in range(2000):
		driver.get(vlist[random.randint(0,2)])
		time.sleep(random.randint(20,40))

for i in range(tabs):
	browser=threading.Thread(target=view,args=(uc.Chrome(),))
	browser.start()

driver.quit()
