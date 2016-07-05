from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = "yourUsername"
pwd = "passwordHere"

driver = webdriver.Firefox()
# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

#elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div")
#elem.click()
#elem = driver.find_element_by_class_name("seeMore")
#elem.click()
#elem = driver.find_element_by_class_name("_1rt")


#elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/ul/li[2]/a/div/div[2]/div/div[2]/div/div[1]/strong/span")
#elem.click()

#send_keys("Hi")
