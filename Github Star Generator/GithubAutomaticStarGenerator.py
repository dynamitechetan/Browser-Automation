import time
import random
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys


for x in range(387,8000000):

	i=random.randint(0,148);

	names=["Nestor-Ohair", "Misty-Meiser", "Nyla-Hockman", "Evalyn-Aoki", "Michal-Mincks", "Maryalice-Railey", "Aubrey-Spengler", "Slyvia-Lucarelli", "Deedee-Bergquist", "Nu-Landrith", "Marilynn-Hansell", "Janelle-Seaberg", "Georgianne-Gott", "Shannan-Ota", "Raelene-Epperly", "Gabriela-Hodges", "Mathew-Samet", "Norah-Gin", "Toshia-Bergevin", "Mitsuko-Edmund", "Izola-Osmun", "Tonette-Vital", "Gwyneth-Blanchard", "Lashonda-Theriot", "Kecia-Alfrey", "Numbers-Tritt", "Lynsey-Bate", "Palmira-Aberle", "Jolynn-Gonyea", "Dino-Bulloch", "Lilliana-Pinkham", "Alyssa-Tice", "Thi-Rickards", "Diedra-Wiltsie", "Jayme-Haus", "Lazaro-Nicks", "Maybell-Perry", "Kandi-Weary", "Maryann-Schrom", "Rashad-Petrucci", "Chauncey-Silvis", "Flo-Eldredge", "Cora-Eber", "Lavelle-Medlen", "Lanelle-Blecha", "Genna-Holcomb", "Tyisha-Asmus", "Eleonora-Iverson", "Coleen-Daquila", "Craig-Beckmann", "Sindy", "Mireille", "Alesha", "Galina", "Corliss", "Towanda", "Abbie", "Katia", "German", "Carina", "Sherly", "Danica", "Ken", "Desmond", "Lekisha", "Elnora", "Lenita", "Douglas", "Billye", "Rocio", "Elvin", "Kenia", "Candida", "Jaye", "Katrina", "Marcel", "Tania", "Kesha", "Brook", "Regena", "Sylvie", "Jae", "Wai", "Madeline", "Adelia", "Savanna", "Jacquiline", "Lottie", "Tamekia", "Paulina", "Blake", "Christi", "Ina", "Jung", "Corinna", "Sophia", "Vanetta", "Marya", "Eloy", "Isobel","Angeline-Fry", "Marianne-Richman", "Ladonna-Mozingo", "Lenard-Pelfrey", "Twyla-Stanforth", "Danielle-Pedretti", "Vennie-Hippert", "Jaleesa-Kinghorn", "Benton-Thrailkill", "Cheri-Soja", "Patti-Loose", "Nakita-Sipe", "Particia-Bober", "Sherry-Beutler", "Kristal-Nez", "Garrett-Galicia", "Toya-Rodriguez", "Rochell-Lajoie", "Li-Violet", "Roberto-Teachout", "Antoine-Bertin", "Amiee-Prestwood", "Dina-Ransdell", "Stephnie-Gift", "Inge-Mayne", "Leonor-Earnest", "Shon-Clary", "Ping-Simmons", "Belia-Keatts", "Malisa-Schank", "Noelia-Collazo", "Maya-Bellini", "Mathew-Benedetto", "Nella-Rainer", "Shad-Cullum", "Kathey-Littlewood", "Carrie-Feiler", "Suzy-Shuler", "Graciela-Podesta", "Thomas-Chavers", "Tonia-Woodland", "Jadwiga-Schreckengost", "Cherrie-Geiser", "Asia-Getman", "Lucilla-Troester", "Gianna-Mcgillis", "Allegra-Carasco", "Marcella-Hintzen", "Grady-Hixson", "Douglass-Kolb"];

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

	time.sleep(10);
	driver.get("http://maildrop.cc/inbox/" + names[i] + str(x));
	driver.find_element_by_xpath("//*[@id='inboxtbl']/tbody/tr[1]/td[2]/a").click();
	time.sleep(10);
	pyautogui.press('tab');
	# time.sleep(1);
	pyautogui.press('tab');
	# time.sleep(1);
	pyautogui.press('tab');
	# time.sleep(1);
	pyautogui.press('tab');
	# time.sleep(1);
	pyautogui.press('tab');
	time.sleep(1);
	
	pyautogui.keyDown('ctrl');
	time.sleep(1);
	# driver.find_element_by_xpath("/html/body/div[2]/div/a").click();
	pyautogui.press('enter');
	pyautogui.keyUp('ctrl');
	time.sleep(10);

	# pyautogui.keyDown('ctrl');
	# time.sleep(1);
	# driver.find_element_by_xpath("/html/body/div[2]/div/a").click();
	# pyautogui.press('w');
	# pyautogui.keyUp('ctrl');

	# driver.find_element_by_xpath("//*[@id='js-pjax-container']/div[1]/div/div/a[2]").click();

	# repo=driver.find_element_by_id("repository_name");
	# repo.send_keys(names[i]);
	# repo.send_keys(Keys.RETURN);

	driver.get("https://github.com/AnupKumarPanwar");
	driver.find_element_by_xpath("//*[@id='js-pjax-container']/div/div/div[2]/div[1]/div/span/span[1]/form/button");
	

	driver.get("https://github.com/AnupKumarPanwar/Ionic-FB-Login-PHP-MySQL-DB-AdMob");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/AnupKumarPanwar/Book-it-to-the-Moon");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/AnupKumarPanwar/Browser-Automation");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();

	

	

	driver.get("https://github.com/AnupKumarPanwar/MoonData");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/TheAlgorithms/C-Plus-Plus/stargazers");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/TheAlgorithms/Scala/stargazers");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();



	driver.get("https://github.com/TheAlgorithms/Python/stargazers");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/dynamitechetan/Project0_Portfolio_App_Udacity");	
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/AnupKumarPanwar/Algorithms");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();


	driver.get("https://github.com/dynamitechetan/Browser-Automation");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();

	driver.get("https://github.com/AnupKumarPanwar/Ionic-Google-Maps-App-to-Locate-Friends");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();

	driver.get("https://github.com/AnupKumarPanwar/FireBase-Chat-App");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();
	

	driver.get("https://github.com/AnupKumarPanwar/NodeJS-SocketIO-Realtime-Chat-App");
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[3]/a[1]").click();
	driver.find_element_by_xpath("//*[@id='js-repo-pjax-container']/div[1]/div[1]/ul/li[2]/div/form[2]/button").click();

	# driver.find_element_by_xpath("//*[@id='user-links']/li[3]/div/div/form/button").click();

	driver.quit();
	
	with open("users.txt", "a") as myfile:
		myfile.write(names[i]+str(x) + "\", \"" );