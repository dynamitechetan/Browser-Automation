from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait


def print_dish_names():
 driver = webdriver.Chrome("D:\chromedriver\chromedriver")
 driver.implicitly_wait(10) 
 driver.get("https://zipongo.com/recipes/category/fruits")
 driver.implicitly_wait(10) 
 dishes=driver.find_elements_by_css_selector('.js-name')
 times=driver.find_elements_by_css_selector('.small-8')
 dictionary={}
 j=0
 for i in dishes:
    dictionary[i.text]=int(times[j].text.split(' ')[2])
    j+=2
 for key in  sorted(dictionary, key=dictionary.get, reverse=False):
  print (key, dictionary[key])
 driver.close()

if __name__ == "__main__":
 print_dish_names()
