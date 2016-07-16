import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


for x in range(3,8000000):

	i=random.randint(0,49);

	names=["Nestor-Ohair", "Misty-Meiser", "Nyla-Hockman", "Evalyn-Aoki", "Michal-Mincks", "Maryalice-Railey", "Aubrey-Spengler", "Slyvia-Lucarelli", "Deedee-Bergquist", "Nu-Landrith", "Marilynn-Hansell", "Janelle-Seaberg", "Georgianne-Gott", "Shannan-Ota", "Raelene-Epperly", "Gabriela-Hodges", "Mathew-Samet", "Norah-Gin", "Toshia-Bergevin", "Mitsuko-Edmund", "Izola-Osmun", "Tonette-Vital", "Gwyneth-Blanchard", "Lashonda-Theriot", "Kecia-Alfrey", "Numbers-Tritt", "Lynsey-Bate", "Palmira-Aberle", "Jolynn-Gonyea", "Dino-Bulloch", "Lilliana-Pinkham", "Alyssa-Tice", "Thi-Rickards", "Diedra-Wiltsie", "Jayme-Haus", "Lazaro-Nicks", "Maybell-Perry", "Kandi-Weary", "Maryann-Schrom", "Rashad-Petrucci", "Chauncey-Silvis", "Flo-Eldredge", "Cora-Eber", "Lavelle-Medlen", "Lanelle-Blecha", "Genna-Holcomb", "Tyisha-Asmus", "Eleonora-Iverson", "Coleen-Daquila", "Craig-Beckmann"];

	driver = webdriver.Chrome()

	driver.get("https://github.com/join?source=header-home");

	# driver.find_element_by_class_name("octicon-star").click();
	
	# driver.find_element_by_xpath("//*[@id='login']/p/a").click();

	user  = driver.find_element_by_id("user_login");
	user.send_keys(names[i] + str(x));
	email = driver.find_element_by_id("user_email");
	email.send_keys(names[i] + str(x) + "@maildrop.cc");
	passw = driver.find_element_by_id("user_password");
	passw.send_keys(names[i]+"@123");
	passw.send_keys(Keys.RETURN)
	driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/div/form/button").click();

	driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div[2]/div/form/a").click();

	driver.get("https://github.com/AnupKumarPanwar/Ionic-FB-Login-PHP-MySQL-DB-AdMob");

	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	# driver.find_element_by_xpath("//*[@id='user-links']/li[3]/div/div/form/button").click();

	driver.quit();
	