from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re

driver = webdriver.Chrome("D:\chromedriver\chromedriver")
driver.get("http://www.gmail.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='Email']").send_keys("dynamitechetan@gmail.com")
driver.find_element_by_id("next").click()
driver.find_element_by_xpath("//*[@id='Passwd']").send_keys("chetankaushik29")
driver.find_element_by_xpath("//*[@id='signIn']").click()
inbox = driver.find_element_by_xpath("//*[contains(@title,'Inbox')]").text

pattern = re.compile("\w+\s+\((\d+)\)")
match = re.search(pattern,inbox)
if match:
    print("Total no of unread mails in your inbox are ",int(match.group(1)))

driver.close()
