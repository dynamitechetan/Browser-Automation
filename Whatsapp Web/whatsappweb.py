from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

def web_driver_load():
	global driver
	ddriver = webdriver.Chrome("D:\chromedriver\chromedriver")

def web_driver_quit():
	driver.quit()

def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(10)


def sendMessage(msg, recepient_list):
	for recep in recepient_list:
		print ("Sending to : ",recep)
		try:
			one_chat = driver.find_element_by_xpath("//span[@title='%s']"%(recep))
		except:
			print ("Unable to find username [%s]"%recep)
			continue
		if one_chat != None:
			try:
				one_chat.click()
				wait(1)
				print ("Chatbox opened for ", recep)
				text_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
				for letter in list(msg):
					text_box.send_keys(letter)
					wait(0.1)
				text_box.send_keys(Keys.RETURN)
			except:
				print ("Unable to send msg [%s] to [%s]"%(msg, recep))
				continue
			print ("Message [%s] sent to [%s]"%(msg, recep))

if __name__ == '__main__':
	number_of_times = 1
	messages = ["""Hello"""]
	recepients = ["Testing"]

	web_driver_load()
	whatsapp_login()

	for i in range(number_of_times):
		for msg in messages:
			print ("[%d]"%(i+1))
			sendMessage(msg, recepients)
	web_driver_quit()
