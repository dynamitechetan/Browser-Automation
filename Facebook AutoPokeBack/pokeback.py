import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

print "Enter your email ID"
email_id = raw_input(">>")
print "Enter your password"
#password = raw_input(">>")
password = getpass.getpass(">>")

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/pokes")
driver.maximize_window()

email = driver.find_element_by_xpath("//label[@for = 'email']")
email.send_keys(email_id)
driver.find_element_by_xpath("//label[@for = 'pass']").click()
passwd = driver.find_element_by_xpath("//label[@for = 'pass']")
passwd.send_keys(password)
passwd.send_keys(Keys.ENTER)


pokes = driver.find_elements_by_link_text('Poke Back')
for poke in pokes:
    poke.click()

driver.find_element_by_id('userNavigationLabel').click()

time.sleep(1)

logout = driver.find_element_by_class_name('_w0d')
logout.submit()


driver.implicitly_wait(2)
driver.close()
