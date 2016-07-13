from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.goibibo.com/")
ele = driver.find_element_by_xpath("//*[@id='gi_class']")
all_options = ele.find_elements_by_tag_name("option")
for option in all_options:
    #printing all options text vlaues
    print (option.text)
    #selecting First Class
    if option.text == 'First Class':
         option.click()
