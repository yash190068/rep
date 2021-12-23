import undetected_chromedriver as uc
import time
import random
import threading
driver = uc.Chrome()

vlist = ['https://youtu.be/6G-pTxdjao4','https://youtu.be/eJeBFr4FgDI','https://youtu.be/iL4kBcNpm2s','https://youtu.be/1V-tQzN6Azw']
tabs = 4

def view(driver):
	for i in range(2000):
		driver.get(vlist[random.randint(0,2)])
		time.sleep(random.randint(2700,3700))

for i in range(tabs):
	browser=threading.Thread(target=view,args=(uc.Chrome(),))
	browser.start()

driver.quit()
