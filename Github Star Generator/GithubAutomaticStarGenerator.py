import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


for x in range(13,8000000):

	driver = webdriver.Chrome()

	driver.get("https://github.com/join?source=header-home");

	# driver.find_element_by_class_name("octicon-star").click();
	
	# driver.find_element_by_xpath("//*[@id='login']/p/a").click();

	user  = driver.find_element_by_id("user_login");
	user.send_keys("User-name12" + str(x));
	email = driver.find_element_by_id("user_email");
	email.send_keys("User-name12" + str(x) + "@maildrop.cc");
	passw = driver.find_element_by_id("user_password");
	passw.send_keys("HelloWorld@123");
	passw.send_keys(Keys.RETURN)
	driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/div/form/button").click();

	driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/div/form/a").click();

	driver.get("https://github.com/AnupKumarPanwar/Ionic-FB-Login-PHP-MySQL-DB-AdMob");

	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();
	# driver.find_element_by_xpath("//*[@id='user-links']/li[3]/div/div/form/button").click();

	driver.quit();
	