from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import threading
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')

vlist = ['https://youtu.be/lUxzjQvNBmg','https://youtu.be/PHBLddvszao','https://youtu.be/uWcyQKQBnXk']
tabs = 4

def view(driver):
	for i in range(2000):
		driver.get(vlist[random.randint(0,2)])
		time.sleep(random.randint(20,40))

for i in range(tabs):
	browser=threading.Thread(target=view,args=(webdriver.Chrome(executable_path='chromedriver',options=option),))
	browser.start()

driver.quit()
